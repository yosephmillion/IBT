import { useEffect, useRef, useState } from "react";
import Dish from "./Dish/Dish";
import Card from "./Card";
import { loadDishes } from "../../api";
import "./Dish/Dish.css";

function Menu() {
  const [category, setCategory] = useState("All");
  const [dishes, setDishes] = useState([]);
  const [cart, setCart] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const searchRef = useRef(null);

  const categories = ["All", "Main", "Vegetarian", "Breakfast", "Side"];

  useEffect(() => {
    searchRef.current?.focus();
  }, []);

  useEffect(() => {
    const controller = new AbortController();

    async function fetchDishes() {
      try {
        setLoading(true);
        setError("");

        const data = await loadDishes(category, controller.signal);

        setDishes(data);
      } catch (error) {
        if (error.name !== "AbortError") {
          setError(error.message);
        }
      } finally {
        if (!controller.signal.aborted) {
          setLoading(false);
        }
      }
    }

    fetchDishes();

    return () => {
      controller.abort();
    };
  }, [category]);

  function updateQuantity(id, amount) {
    setCart((currentCart) => {
      const currentQuantity = currentCart[id] || 0;

      return {
        ...currentCart,
        [id]: Math.max(0, currentQuantity + amount),
      };
    });
  }

  const totalDishCount = Object.values(cart).reduce(
    (total, quantity) => total + quantity,
    0,
  );

  const totalPrice = dishes.reduce(
    (total, dish) => total + dish.price * (cart[dish.id] || 0),
    0,
  );

  if (loading) {
    return <p>Loading dishes...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div className="menu">
      <div className="io">
        <h1 className="total">🛒 {totalDishCount}</h1>
      </div>

      <input ref={searchRef} type="text" placeholder="Search dishes..." />

      <div className="categories">
        {categories.map((cat) => (
          <button
            key={cat}
            onClick={() => setCategory(cat)}
            className={cat === category ? "active" : ""}
          >
            {cat}
          </button>
        ))}
      </div>

      {dishes.map((dish) => (
        <Card key={dish.id}>
          <Dish
            {...dish}
            count={cart[dish.id] || 0}
            onIncrease={() => updateQuantity(dish.id, 1)}
            onDecrease={() => updateQuantity(dish.id, -1)}
          />
        </Card>
      ))}
    </div>
  );
}

export default Menu;
