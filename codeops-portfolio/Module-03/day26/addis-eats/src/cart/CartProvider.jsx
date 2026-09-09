import { createContext, useReducer, useMemo } from "react";
import { cartReducer } from "./cartReducer";

export const CartContext = createContext();

export default function CartProvider({ children }) {
  const [items, dispatch] = useReducer(cartReducer, {});

  const total = Object.values(items).reduce(
    (sum, item) => sum + item.quantity,
    0,
  );

  const value = useMemo(
    () => ({
      items,
      dispatch,
      total,
    }),
    [items, total],
  );

  return <CartContext.Provider value={value}>{children}</CartContext.Provider>;
}
