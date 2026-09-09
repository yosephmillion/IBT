export function cartReducer(state, action) {
  switch (action.type) {
    case "add": {
      const dish = action.payload;

      return {
        ...state,
        [dish.id]: {
          ...dish,
          quantity: (state[dish.id]?.quantity || 0) + 1,
        },
      };
    }

    case "remove": {
      const dish = state[action.payload];

      if (!dish) return state;

      if (dish.quantity === 1) {
        const newState = { ...state };
        delete newState[action.payload];
        return newState;
      }

      return {
        ...state,
        [action.payload]: {
          ...dish,
          quantity: dish.quantity - 1,
        },
      };
    }

    case "clear":
      return {};

    default:
      return state;
  }
}
