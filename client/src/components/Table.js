import React, { useMemo } from "react";
import { useTable } from "react-table";

import { terroristColumns, ctColumns } from "./Columns";

const Table = ({ terrorists, ct }) => {
  const data = useMemo(() => (terrorists ? terrorists : ct), []);
  const columns = useMemo(
    () => (terrorists ? terroristColumns : ctColumns),
    []
  );

  const tableInstance = useTable({
    columns,
    data,
  });

  const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    tableInstance;

  return (
    <table
      className="text-white w-96 h-80 text-center m-10"
      {...getTableBodyProps()}
    >
      <thead>
        {headerGroups.map((headerGroup) => (
          <tr {...headerGroup.getFooterGroupProps()}>
            {headerGroup.headers.map((column) => (
              <th className="p-1.5 border" {...column.getHeaderProps()}>
                {column.render("Header")}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody {...getTableBodyProps}>
        {rows.map((row) => {
          prepareRow(row);
          return (
            <tr {...row.getRowProps()}>
              {row.cells.map((cell) => (
                <td className="p-1 border text-center" {...cell.getCellProps()}>{cell.render("Cell")}</td>
              ))}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};

export default Table;
