import axios from "axios";

const backendPortNumber = "8080";
const serverUrl =
  "http://" + window.location.hostname + ":" + backendPortNumber + "/";

async function get(endpoint) {
  console.log(`%cGET 요청 ${serverUrl + endpoint}`, "color: a25cd1");

  return axios.get(serverUrl + endpoint);
}

export { get };
