import React, { useEffect } from "react";
import { connect } from "react-redux";
import * as actions from "../actions";

const App = ({ fetchStatistics, statistics }) => {
  console.log("🚀 ~ file: App.js ~ line 6 ~ App ~ statistics", statistics)
  useEffect(() => {
    fetchStatistics();
  }, []);
  return (
    <div className="bg-blast-bg w-screen h-screen p-5">
      <div className="text-5xl text-blast-yellow text-center">
        Match statistics
      </div>
    </div>
  );
};

const mapStateToProps = ({ statistics }) => {
  return {
    statistics,
  };
};

export default connect(mapStateToProps, actions)(App);
