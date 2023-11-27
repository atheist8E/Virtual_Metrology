import { lazy } from 'react';

// project import
import Loadable from 'components/Loadable';
import MainLayout from 'layout/MainLayout';

// render - dashboard
const Dashboard = Loadable(lazy(() => import('pages/dashboard')));
const Extractor = Loadable(lazy(() => import('pages/extractor')));


// ==============================|| MAIN ROUTING ||============================== //

const MainRoutes = {
  path: '/',
  element: <MainLayout />,
  children: [
    {
      path: '/',
      element: <Dashboard />
    },
    {
        path: 'dashboard',
        element: <Dashboard />
    },
    {
        path: 'extractor',
        element: <Extractor />
    },
  ]
};

export default MainRoutes;
