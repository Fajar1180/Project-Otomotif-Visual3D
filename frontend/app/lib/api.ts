export const BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function apiRequest(
  path: string,
  init: RequestInit = {}
): Promise<Response> {
  const res = await fetch(`${BASE_URL}${path}`, {
    headers: { "Content-Type": "application/json", ...init.headers },
    ...init,
  });
  return res;
}

export async function apiJson<T = unknown>(
  path: string,
  init: RequestInit = {}
): Promise<T> {
  const res = await apiRequest(path, init);
  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(text || `API error ${res.status}`);
  }
  return (await res.json()) as T;
}
