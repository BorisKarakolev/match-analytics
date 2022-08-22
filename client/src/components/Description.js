import React from "react";

const Description = ({ statistics }) => {
  return (
    <div className="w-2/4 flex flex-col text-center items-center p-10">
      <span className="text-4xl text-crocobot-eye mb-10">
        {statistics.won.slice(0, -1)}
      </span>
      <span className="text-white font-sans break-normal mb-5">
        After a long game we are happy to log the match by very competitive
        CS:GO professional teams. Below you can see some of the statistics.
      </span>
      <ul className="list-disc text-white text-start place-self-center">
        <li>{statistics.all_time} minutes match</li>
        <li>{statistics.rounds_played} rounds played</li>
        <li>map {statistics.map}</li>
        <li>Average round length is {statistics.avg_round_length} seconds</li>
      </ul>
    </div>
  );
};

export default Description;
