function State({ count, onIncrease, onDecrease }) {
    return (
        <div className="quantity">

            <button onClick={onDecrease}>
                -
            </button>

            <span>{count}</span>

            <button onClick={onIncrease}>
                +
            </button>

        </div>
    );
}

export default State;