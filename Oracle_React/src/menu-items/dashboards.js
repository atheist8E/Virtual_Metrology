// assets
import { 
  ProfileOutlined,
  LineChartOutlined,
  DotChartOutlined,
  WarningOutlined,
  ContainerOutlined  } from '@ant-design/icons';

// icons
const icons = {
  ProfileOutlined,
  LineChartOutlined,
  DotChartOutlined,
  WarningOutlined,
  ContainerOutlined
};

// ==============================|| MENU ITEMS - DASHBOARD ||============================== //

const dashboards = {
  id: 'group-dashboard',
  title: 'Dashboards',
  type: 'group',
  children: [
    {
      id: 'dashboard',
      title: 'Dashboard',
      type: 'item',
      url: 'dashboards/dashboard',
      icon: icons.ProfileOutlined,
      breadcrumbs: false
    },
    {
      id: 'periodical',
      title: 'Periodical',
      type: 'item',
      url: 'dashboards/periodical',
      icon: icons.LineChartOutlined,
      breadcrumbs: false
    },
    {
      id: 'daily',
      title: 'Daily',
      type: 'item',
      url: 'dashboards/daily',
      icon: icons.DotChartOutlined,
      breadcrumbs: false
    },
    {
      id: 'anomaly',
      title: 'Anomaly',
      type: 'item',
      url: 'dashboards/anomaly',
      icon: icons.WarningOutlined,
      breadcrumbs: false
    },
    {
      id: 'historical',
      title: 'Historical',
      type: 'item',
      url: 'dashboards/historical',
      icon: icons.ContainerOutlined,
      breadcrumbs: false
    }
  ]
};

export default dashboards;
