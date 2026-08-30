import State from "../State";

function Dish({
    name,
    price,
    image,
    description,
    spicy,
    count,
    onIncrease,
    onDecrease
}) {
    return (
        <div className="dish">

            {image && (
                <img src={image} alt={name} />
            )}

            <div className="dish-info">

                <h2>{name}</h2>

                {description && (
                    <p>{description}</p>
                )}

                <p>{price} ETB</p>

                {spicy && (
                    <span className="spicy">
                        🌶️ SPICY
                    </span>
                )}

                <State
                    count={count}
                    onIncrease={onIncrease}
                    onDecrease={onDecrease}
                />

            </div>

        </div>
    );
}

export default Dish;