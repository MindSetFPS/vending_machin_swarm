import Image from "next/image";
import { Button } from '@nextui-org/button';
import Title from "@/components/Title";
import Subtitle from "@/components/Subtitle";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center p-24">
      <Title>Maneja tus maquinas expendedoras desde cualquier lugar</Title>
      <Subtitle>Estadisticas, ventas y más desde la palma de tu mano.</Subtitle>
    </main>
  );
}

