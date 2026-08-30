function Categories({ categories, category, setCategory }) {
    return (
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
    );
}

export default Categories;