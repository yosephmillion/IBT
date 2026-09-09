import { useContext } from "react";
import { CartContext } from "../cart/CartProvider";

export default function Dish({ dish }) {
  const { dispatch, items } = useContext(CartContext);

  const quantity = items[dish.id]?.quantity || 0;

  return (
    <div className="dish">
      <h3>{dish.name}</h3>

      <p>{dish.category}</p>

      <strong>${dish.price}</strong>

      <div>
        <button
          onClick={() =>
            dispatch({
              type: "remove",
              payload: dish.id,
            })
          }
        >
          -
        </button>

        <span>{quantity}</span>

        <button
          onClick={() =>
            dispatch({
              type: "add",
              payload: dish,
            })
          }
        >
          +
        </button>
      </div>
    </div>
  );
}
