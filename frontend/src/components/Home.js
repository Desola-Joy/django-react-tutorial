import {React, useEffect, useState} from 'react'
import AxiosInstance from './Axios'
import {DataGrid} from '@mui/x-data-grid'
import Paper from '@mui/material/Paper';

const Home = () => {


  const [MyData, setMyData] = useState()


  const GetData = () => {
    AxiosInstance.get("project/")
    .then((res) =>{
      setMyData(res.data)
      console.log(res.data)
    })
  }

  useEffect(() => {
    GetData();
  },[] )


const columns = [
  { field: 'id', headerName: 'ID', width: 70 },
  { field: 'name', headerName: 'Name', width: 150 },
  { field: 'status', headerName: 'Status', width: 150 },
  {
    field: 'comments',
    headerName: 'Comments',
    width: 200,
  },
  {
    field: 'start_date',
    headerName: 'Start Date',
    width: 160,
  },
  {
    field: 'end_date',
    headerName: 'End Date',
    width: 200,
  },
];

// valueGetter: (value, row) => `${row.firstName || ''} ${row.lastName || ''}`

const paginationModel = { page: 0, pageSize: 5 };

  return (
    <Paper sx={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={MyData}
        columns={columns}
        initialState={{ pagination: { paginationModel } }}
        pageSizeOptions={[5, 10]}
        checkboxSelection
        sx={{ border: 0 }}
      />
    </Paper>
  );

  return <div>Home Component</div>;

}

export default Home