import Dish from "./Dish/Dish";
import Card from "./Card";
import dishlist from "./data/data";
import "./Dish/Dish.css";

function Menu({ category }) {

    category = "Main"

    const shown = dishlist.filter(
        (dish) => dish.category === category
    );

    if (shown.length === 0) {
        return <p>No {category} dishes.</p>;
    }

    return (
        <div className="menu">
            {shown.map((dish) => (
                <Card key={dish.id}>
                    <Dish {...dish} />
                </Card>
            ))}
        </div>
    );
}

export default Menu;