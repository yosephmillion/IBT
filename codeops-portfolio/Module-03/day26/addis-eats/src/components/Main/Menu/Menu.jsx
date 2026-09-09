import { useMemo, useState } from "react";

import useFetch from "./hooks/useFetch";
import Dish from "./components/Dish";

export default function Menu() {
  const { data, loading, error } = useFetch("YOUR_API_URL_HERE");

  const [category, setCategory] = useState("All");

  const categories = useMemo(() => {
    return ["All", ...new Set(data.map((dish) => dish.category))];
  }, [data]);

  const filteredDishes = useMemo(() => {
    if (category === "All") {
      return data;
    }

    return data.filter((dish) => dish.category === category);
  }, [data, category]);

  if (loading) {
    return <h2>Loading...</h2>;
  }

  if (error) {
    return <h2>Error: {error}</h2>;
  }

  return (
    <section>
      <div className="categories">
        {categories.map((cat) => (
          <button key={cat} onClick={() => setCategory(cat)}>
            {cat}
          </button>
        ))}
      </div>

      <div className="menu">
        {filteredDishes.map((dish) => (
          <Dish key={dish.id} dish={dish} />
        ))}
      </div>
    </section>
  );
}
