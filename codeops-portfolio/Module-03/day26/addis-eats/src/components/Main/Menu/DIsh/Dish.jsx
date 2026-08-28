import PropTypes from "prop-types";

function Dish({ name, price, category, spicy}) {
    return (
        <div className="dish">
            <div className="info">
                <h3>{name}</h3>
                <h4>{price} ETB</h4>
                <p>{category}</p>
                {spicy && <span className="spicy">🌶️SPICY</span>}
            </div>
        </div>
    );
}

Dish.propTypes = {
    name: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    category: PropTypes.string.isRequired,
    spicy: PropTypes.bool,
}

export default Dish;

