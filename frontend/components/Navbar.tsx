// import React from "react";
// 'use client'
import { Navbar, NavbarBrand, NavbarContent, NavbarItem, Link, Button } from "@nextui-org/react";
import { AcmeLogo } from "./Logo";

import { useRouter } from "next/router";
import { useEffect } from "react";

export default function Nav() {

  const router = useRouter()

  useEffect(() => {
    if (!router.isReady) {
      return
    } 
  }, [router.isReady])

  return (
    <Navbar>
      <NavbarBrand>
        <Link color="foreground" href="/">
          <AcmeLogo />
          <p className="font-bold text-inherit">ACME</p>
        </Link>
      </NavbarBrand>
      <NavbarContent className="hidden sm:flex gap-4" justify="center">
        <NavbarItem>
          <Link color="foreground" href="/machines">
            Vending Machines
          </Link>
        </NavbarItem>

        <NavbarItem isActive={false}>
          <Link href="/incidencias" aria-current="page">
            Incidencias
          </Link>
        </NavbarItem>
        <NavbarItem isActive>
          <Link href="/products" >
            Products
          </Link>
        </NavbarItem>
      </NavbarContent>
      <NavbarContent justify="end">
        <NavbarItem className="hidden lg:flex hover:underline">
          <Link href="#">Login</Link>
        </NavbarItem>
        <NavbarItem>
          <Button as={Link} color="primary" href="#" variant="flat">
            Sign Up
          </Button>
        </NavbarItem>
      </NavbarContent>
    </Navbar>
  );
}
