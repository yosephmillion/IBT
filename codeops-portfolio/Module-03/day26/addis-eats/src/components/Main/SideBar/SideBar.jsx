import { useContext } from "react";

import { CartContext } from "../cart/CartProvider";

export default function SideBar() {
  const { items, dispatch, totalPrice } = useContext(CartContext);

  const cartItems = Object.values(items);

  return (
    <aside className="side-bar">
      <h2>Your Cart</h2>

      {cartItems.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
          <div className="cart-items">
            {cartItems.map((item) => (
              <div className="cart-item" key={item.id}>
                <div>
                  <strong>{item.name}</strong>

                  <p>
                    ${item.price} × {item.quantity}
                  </p>
                </div>

                <div>
                  <button
                    onClick={() =>
                      dispatch({
                        type: "remove",
                        payload: item.id,
                      })
                    }
                  >
                    -
                  </button>

                  <span>{item.quantity}</span>

                  <button
                    onClick={() =>
                      dispatch({
                        type: "add",
                        payload: item,
                      })
                    }
                  >
                    +
                  </button>
                </div>
              </div>
            ))}
          </div>

          <hr />

          <h3>Total: ${totalPrice.toFixed(2)}</h3>

          <button
            onClick={() =>
              dispatch({
                type: "clear",
              })
            }
          >
            Clear Cart
          </button>
        </>
      )}
    </aside>
  );
}
