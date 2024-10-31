// ./static/js/model.js
class DataModel {
    constructor(apiEndpoint) {
        this.apiEndpoint = apiEndpoint;
        this.data = [];
        this.subscribers = [];
    }

    // Fetches data from API and notifies subscribers
    fetchData() {
        fetch(this.apiEndpoint)
            .then(response => response.json())
            .then(json => {
                this.data = json.data;
                this.notifySubscribers();
            })
            .catch(error => console.error('Error loading data:', error));
    }

    // Subscribe function for table/chart updates
    subscribe(callback) {
        this.subscribers.push(callback);
    }

    // Notify all subscribers of data changes
    notifySubscribers() {
        this.subscribers.forEach(callback => callback(this.data));
    }
}
