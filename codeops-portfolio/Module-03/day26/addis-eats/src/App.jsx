import CartProvider from "./cart/CartProvider";

import Header from "./components/Header/Header";
import SideBar from "./components/SideBar/SideBar";

import Menu from "./components/Main/Menu/Menu";

export default function App() {
  return (
    <CartProvider>
      <Header />

      <main className="app">
        <Menu />

        <SideBar />
      </main>
    </CartProvider>
  );
}
