import React from 'react';
import '../../styles/Collapse.scss'
import {Link} from "react-router-dom";
import ReactTable from "react-table";


let renderMachine = function (val) {
  return (
    <span>{val.ip_addr} {(val.domain_name ? " (".concat(val.domain_name, ")") : "")}</span>
  )
};

let formatScanned = function (data){
  let result = [];
  for(let service in data.machine.services){
    let scanned_service = {'machine': data.machine,
                           'service': {'endpoint': data.machine.services[service].endpoint,
                                       'name': data.machine.services[service].display_name,
                                       'time': data.machine.services[service].time}};
    result.push(scanned_service)
  }
  return result
};

const columns = [
  {
    columns: [
      {Header: 'Machine', id: 'machine', accessor: x => renderMachine(x.machine),
        style: { 'whiteSpace': 'unset' }, width: 200},
      {Header: 'Time', id: 'time', accessor: x => x.service.time, style: { 'whiteSpace': 'unset' }, width: 170},
      {Header: 'Port/url', id: 'port', accessor: x =>x.service.endpoint, style: { 'whiteSpace': 'unset' }},
      {Header: 'Service', id: 'service', accessor: x => x.service.name, style: { 'whiteSpace': 'unset' }}
      ]
  }
];

class T1210 extends React.Component {

  constructor(props) {
    super(props);
  }

  renderScannedServices(data) {
    return (
      <div>
        <br/>
        <div>Found services: </div>
        <ReactTable
            columns={columns}
            data={data}
            showPagination={false}
            defaultPageSize={data.length}
        />
      </div>)
  }

  renderExploitedServices(data) {
    return (
      <div>
        <br/>
        <div>Exploited services: </div>
        <ReactTable
            columns={columns}
            data={data}
            showPagination={false}
            defaultPageSize={data.length}
        />
      </div>)
  }

  render() {
    let scanned_services = this.props.data.scanned_services.map(formatScanned).flat();
    console.log(scanned_services);
    console.log(this.props.data);
    return (
      <div>
        <div>{this.props.data.message}</div>
        {scanned_services.length > 0 ?
          this.renderScannedServices(scanned_services) : ''}
        {this.props.data.exploited_services.length > 0 ?
          this.renderExploitedServices(this.props.data.exploited_services) : ''}
        <div className="attack-report footer-text">
          To get more info about scanned and exploited machines view <Link to="/report">standard report.</Link>
        </div>
      </div>
    );
  }
}

export default T1210;
