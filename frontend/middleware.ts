import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

const PUBLIC_PATHS = ["/login", "/register", "/forgot-password", "/verify-email", "/"];

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const token = request.cookies.get("otomotif_auth_token")?.value;

  const isPublic = PUBLIC_PATHS.includes(pathname);

  // Jika ada token disimpan di cookie middleware, izinkan akses halaman publik tapi redirect ke / kalau sudah login
  if (isPublic && token) {
    return NextResponse.redirect(new URL("/", request.url));
  }

  // Jika bukan publik dan tidak ada token -> redirect ke login
  if (!isPublic && !token) {
    const loginUrl = new URL("/login", request.url);
    loginUrl.searchParams.set("callbackUrl", pathname);
    return NextResponse.redirect(loginUrl);
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!_next|api|_vercel|.*\\..*).*)"],
};
