import React, { useEffect, useState } from "react";
import { connect } from "react-redux";
import * as actions from "../actions";

import Table from "./Table";

const App = ({ fetchStatistics, statistics }) => {
  console.log("🚀 ~ file: App.js ~ line 6 ~ App ~ statistics", statistics);
  useEffect(() => {
    fetchStatistics();
  }, []);

  if (!statistics)
    return (
      <div className="text-5xl text-blast-yellow bg-blast-bg text-center w-screen h-screen p-10">
        Sorry, problem with getting the statistics
      </div>
    );

  return (
    <div className="bg-blast-bg w-screen h-screen p-10">
      <div className="text-6xl text-blast-yellow text-center">
        {statistics.teams[0]} vs {statistics.teams[1]}
      </div>
      <div>
        <Table terrorists={statistics.players?.terrorists} />
        <Table ct={statistics.players?.ct} />
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
