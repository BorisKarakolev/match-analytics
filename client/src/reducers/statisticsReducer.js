import { FETCH_STATISTICS } from "../actions/types";

export default (state = null, action) => {
  switch (action.type) {
    case FETCH_STATISTICS:
      return action.payload.data || false;
    default:
      return state;
  }
};