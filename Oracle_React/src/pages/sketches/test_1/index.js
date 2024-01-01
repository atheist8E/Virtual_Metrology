import { Grid } from '@mui/material';

// project import
import MainCard from 'components/MainCard';

// ==============================|| DASHBOARD - DEFAULT ||============================== //

const Test_1 = () => {

  return (
    <Grid item xs={12}>
      <MainCard sx={{ mt: 2 }} content={false}>
      </MainCard>
    </Grid>
  );
};

export default Test_1;
