import { useContext } from "react";
import { CartContext } from "../cart/CartProvider";

export default function Header() {
  const { total } = useContext(CartContext);

  return (
    <header className="header">
      <h1>Addis Eats</h1>

      <div className="cart-badge">🛒 {total}</div>
    </header>
  );
}
