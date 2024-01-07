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
      title: 'Newsfeed',
      type: 'item',
      url: 'dashboards/dashboard',
      icon: icons.ProfileOutlined,
      breadcrumbs: false
    },
    {
      id: 'daily',
      title: 'Daily Analysis',
      type: 'item',
      url: 'dashboards/daily',
      icon: icons.DotChartOutlined,
      breadcrumbs: false
    },
    {
      id: 'periodical',
      title: 'Periodical Analysis',
      type: 'item',
      url: 'dashboards/periodical',
      icon: icons.LineChartOutlined,
      breadcrumbs: false
    },
    {
      id: 'anomaly',
      title: 'Anomaly Detection',
      type: 'item',
      url: 'dashboards/anomaly',
      icon: icons.WarningOutlined,
      breadcrumbs: false
    },
    {
      id: 'historical',
      title: 'Legacy Patterns',
      type: 'item',
      url: 'dashboards/historical',
      icon: icons.ContainerOutlined,
      breadcrumbs: false
    }
  ]
};

export default dashboards;
