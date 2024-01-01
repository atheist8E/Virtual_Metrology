import { Grid } from '@mui/material';

// project import
import EnhancedTable from './EnhancedTable';
import MainCard from 'components/MainCard';

// ==============================|| DASHBOARD - DEFAULT ||============================== //

const Test_0 = () => {

  return (
    // <Grid item xs={12}>
    //   <Grid container alignItems="center" justifyContent="space-between">
    //     <Grid item>
    //       <Typography variant="h5">Recent Orders</Typography>
    //     </Grid>
    //     <Grid item />
    //   </Grid>
    //   <MainCard sx={{ mt: 2 }} content={false}>
    //     <EnhancedTable />
    //   </MainCard>
    // </Grid>
    <Grid item xs={12}>
      <MainCard sx={{ mt: 2 }} content={false}>
        <EnhancedTable />
      </MainCard>
    </Grid>
    
  );
};

export default Test_0;
