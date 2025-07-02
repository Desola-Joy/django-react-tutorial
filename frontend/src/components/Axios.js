import axios from 'axios'

const baseURL = 'http://localhost:8000/api/';
const AxiosInstance = axios.create({
    baseURL: baseURL,
    timeout: 5000, 
    headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
    }
})

export default AxiosInstance