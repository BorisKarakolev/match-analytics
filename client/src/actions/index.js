import axios from 'axios'
import { FETCH_STATISTICS } from './types'

export const fetchStatistics = () => async (dispatch) =>
  dispatch({ type: FETCH_STATISTICS, payload: await axios.get("http://localhost:4200/") });