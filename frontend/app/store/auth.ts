import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";

export interface User {
  id: string;
  email: string;
  full_name?: string | null;
}

export interface AuthTokens {
  access_token: string;
  refresh_token: string;
  token_type: string;
}

interface AuthState {
  user: User | null;
  tokens: AuthTokens | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;
  setAuth: (user: User, tokens: AuthTokens) => void;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string, full_name?: string) => Promise<void>;
  refresh: () => Promise<void>;
  logout: () => void;
  clearError: () => void;
}

const STORAGE_KEY = "auth-storage";
const COOKIE_KEY = "otomotif_auth_token";

function syncCookie(tokens: AuthTokens | null) {
  if (typeof document === "undefined") return;
  if (tokens?.access_token) {
    document.cookie = `${COOKIE_KEY}=${tokens.access_token}; path=/; max-age=604800; SameSite=Lax`;
  } else {
    document.cookie = `${COOKIE_KEY}=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT`;
  }
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      user: null,
      tokens: null,
      isAuthenticated: false,
      isLoading: false,
      error: null,

      setAuth: (user, tokens) => {
        syncCookie(tokens);
        set({ user, tokens, isAuthenticated: true, error: null });
      },

      login: async (email, password) => {
        set({ isLoading: true, error: null });
        try {
          const data = await fetch(
            `${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/api/v1/auth/login`,
            {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ email, password }),
            }
          );
          if (!data.ok) {
            const err = await data.json().catch(() => ({}));
            throw new Error(err?.detail || err?.message || "Login gagal");
          }
          const json = (await data.json()) as {
            access_token: string;
            refresh_token: string;
            token_type: string;
            user: User;
          };
          syncCookie({
            access_token: json.access_token,
            refresh_token: json.refresh_token,
            token_type: json.token_type,
          });
          set({
            user: json.user,
            tokens: {
              access_token: json.access_token,
              refresh_token: json.refresh_token,
              token_type: json.token_type,
            },
            isAuthenticated: true,
            isLoading: false,
            error: null,
          });
        } catch (e: any) {
          set({ error: e.message, isLoading: false });
          throw e;
        }
      },

      register: async (email, password, full_name) => {
        set({ isLoading: true, error: null });
        try {
          const data = await fetch(
            `${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/api/v1/auth/register`,
            {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ email, password, full_name }),
            }
          );
          if (!data.ok) {
            const err = await data.json().catch(() => ({}));
            throw new Error(err?.detail || err?.message || "Registrasi gagal");
          }
          const json = (await data.json()) as {
            access_token: string;
            refresh_token: string;
            token_type: string;
            user: User;
          };
          syncCookie({
            access_token: json.access_token,
            refresh_token: json.refresh_token,
            token_type: json.token_type,
          });
          set({
            user: json.user,
            tokens: {
              access_token: json.access_token,
              refresh_token: json.refresh_token,
              token_type: json.token_type,
            },
            isAuthenticated: true,
            isLoading: false,
            error: null,
          });
        } catch (e: any) {
          set({ error: e.message, isLoading: false });
          throw e;
        }
      },

      refresh: async () => {
        const { tokens } = get();
        if (!tokens?.refresh_token) return;
        try {
          const data = await fetch(
            `${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/api/v1/auth/refresh`,
            {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ refresh_token: tokens.refresh_token }),
            }
          );
          if (!data.ok) throw new Error("Refresh gagal");
          const json = (await data.json()) as { access_token: string; token_type: string };
          set({
            tokens: {
              ...tokens,
              access_token: json.access_token,
              token_type: json.token_type,
            },
          });
          syncCookie(get().tokens);
        } catch (e: any) {
          get().logout();
        }
      },

      logout: () => {
        syncCookie(null);
        set({
          user: null,
          tokens: null,
          isAuthenticated: false,
          error: null,
        });
      },

      clearError: () => set({ error: null }),
    }),
    {
      name: STORAGE_KEY,
      storage: createJSONStorage(() => localStorage),
      partialize: (state) => ({ user: state.user, tokens: state.tokens, isAuthenticated: state.isAuthenticated }),
    }
  )
);
