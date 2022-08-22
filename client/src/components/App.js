import React, { useEffect } from "react";
import { connect } from "react-redux";
import * as actions from "../actions";

import Description from "./Description";
import Table from "./Table";

const App = ({ fetchStatistics, statistics }) => {
  useEffect(() => {
    fetchStatistics();
  }, []);

  if (!statistics)
    return (
      <div className="text-5xl text-blast-yellow text-center w-full h-full p-10">
        Sorry, problem with getting the statistics
      </div>
    );

  return (
    <div className="bg-blast-bg w-full h-full p-10 flex flex-col items-center lg:items-start">
      <div className="text-6xl text-blast-yellow text-center mb-10 place-self-center">
        {statistics.teams[0]} {statistics.score} {statistics.teams[1]}
      </div>
      <div className="flex flex-col items-center lg:flex-row">
        <div className="flex flex-col w-2/4 items-center">
          <Table terrorists={statistics.players?.terrorists} />
          <Table ct={statistics.players?.ct} />
        </div>
        <Description statistics={statistics} />
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
