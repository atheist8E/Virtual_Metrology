// assets
import { DashboardOutlined } from '@ant-design/icons';

// icons
const icons = {
  DashboardOutlined
};

// ==============================|| MENU ITEMS - DASHBOARD ||============================== //

const extractor = {
  id: 'group-laboratory',
  title: 'Laboratory',
  type: 'group',
  children: [
    {
      id: 'extractor',
      title: 'Data Extractor',
      type: 'item',
      url: '/extractor',
      icon: icons.DashboardOutlined,
      breadcrumbs: false
    }
  ]
};

export default extractor;
