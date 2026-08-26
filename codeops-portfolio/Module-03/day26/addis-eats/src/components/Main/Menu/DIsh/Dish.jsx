function Dish({ name, price }) {
    return (
        <div className="dish">
            <div className="info">
                <h2>{name}</h2>
                <h3>{price} ETB</h3>
            </div>
        </div>
    );
}

export default Dish;