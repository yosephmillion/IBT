import { useState } from "react";
import Dish from "./DIsh/Dish";
import Card from "./Card";
import dishlist from "./data/data";
import "./Dish/Dish.css";

function Menu() {
    const [category, setCategory] = useState("All");
    const [cart, setCart] = useState({});

    const categories = [
        "All",
        "Main",
        "Vegetarian",
        "Breakfast",
        "Side"
    ];

    const shown =
        category === "All"
            ? dishlist
            : dishlist.filter((dish) => dish.category === category);

    function updateQuantity(id, amount) {
        setCart((currentCart) => {
            const currentQuantity = currentCart[id] || 0;

            return {
                ...currentCart,
                [id]: Math.max(0, currentQuantity + amount)
            };
        });
    }

    const totalDishCount = Object.values(cart).reduce(
        (total, quantity) => total + quantity,
        0
    );

    const totalPrice = dishlist.reduce(
        (total, dish) =>
            total + dish.price * (cart[dish.id] || 0),
        0
    );

    return (
        <div className="menu">

            <h2 className="total">
                🛒 {totalDishCount}
            </h2>

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
            {shown.map((dish) => (
                <Card key={dish.id}>
                    <Dish
                        {...dish}
                        count={cart[dish.id] || 0}
                        onIncrease={() =>
                            updateQuantity(dish.id, 1)
                        }
                        onDecrease={() =>
                            updateQuantity(dish.id, -1)
                        }
                    />
                </Card>
            ))}
            <h3>
                Total: {totalPrice} ETB
            </h3>

        </div>
    );
}

export default Menu;