import cv2
import folium
import numpy as np
from sklearn.cluster import KMeans
import tensorflow as tf
from tensorflow.keras import layers
from datetime import datetime
import os
import random
from flask import Flask, render_template, request, jsonify
import random


class WasteClassifier:
    def __init__(self):
        self.model = self.create_model()
        self.class_names = ['organic', 'plastic', 'metal', 'paper']
        
    def create_model(self):
        model = tf.keras.Sequential([
            layers.Rescaling(1./255, input_shape=(224, 224, 3)),
            layers.Conv2D(16, 3, activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, activation='relu'),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dense(4, activation='softmax')
        ])
        model.compile(optimizer='adam',
                     loss='sparse_categorical_crossentropy',
                     metrics=['accuracy'])
        return model
    
    def train(self, epochs=5):
        # Generate synthetic data
        X = np.random.random((100, 224, 224, 3))
        y = np.random.randint(0, 4, 100)
        self.model.fit(X, y, epochs=epochs)
        
    def predict(self, image_path):
        img = cv2.resize(cv2.imread(image_path), (224, 224))
        return self.class_names[np.argmax(self.model.predict(np.array([img])))]


class RouteOptimizer:

    def __init__(self, bins):
        self.bins = bins
        self.map = folium.Map(location=[12.9716, 77.5946], zoom_start=12)
        self.warehouse = (12.9716, 77.5946)  # Central warehouse coordinates

        
    def optimize(self):
        
        coords = np.array([[b['lat'], b['lon']] for b in self.bins])
        n_clusters = min(5, max(2, len(coords) // 20))
        kmeans = KMeans(n_clusters=n_clusters).fit(coords)
        
        colors = ['grey', 'orange', 'yellow', '#0096FF', 'red'][:n_clusters]
        waste_types = ['Organic', 'Plastic', 'Metal', 'Paper', 'Mixed']


        folium.Marker(
            self.warehouse,
            popup="<b>Central Warehouse</b>",
            icon=folium.Icon(icon='industry', prefix='fa')
        ).add_to(self.map)
        
        for idx, bin_data in enumerate(self.bins):
            
            # Create custom numbered icon
            icon = folium.DivIcon(
                icon_size=(30, 30),
                icon_anchor=(15, 15),
                html=f"""
                <div style="
                    background: {colors[kmeans.labels_[idx]]};
                    width: 30px;
                    height: 30px;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: black;
                    font-weight: bold;
                    border: 2px solid black;
                ">
                    {bin_data['id']}
                </div>
                """
            )
            
            folium.Marker(
                [bin_data['lat'], bin_data['lon']],
                popup=folium.Popup(f"""
                    <div style="font-family: Arial; width: 150px">
                        <h4 style="margin:0">Bin {bin_data['id']}</h4>
                        <p style="margin:5px 0">
                            Status: <span style="color:{'red' if bin_data['fill_level']>80 else 'orange' if bin_data['fill_level']>50 else 'green'}; 
                            font-weight:bold">
                            {bin_data['fill_level']}% full
                            </span>
                        </p>
                        <p style="margin:5px 0"><b>Last emptied:</b> {bin_data['last_emptied']} days ago</p>
                        <p style="margin:5px 0"><b>Waste type:</b> {waste_types[kmeans.labels_[idx]]}</p>
                    </div>
                """, max_width=200),
                icon=icon
            ).add_to(self.map)

        '''immediate_bins = [b for b in self.bins if b['fill_level'] > 80]
        if immediate_bins:
            immediate_order = []
            remaining = immediate_bins.copy()
            current = np.array(self.warehouse)
            while remaining:
                next_bin = min(remaining, key=lambda b: np.linalg.norm(np.array([b['lat'], b['lon']]) - current))
                immediate_order.append(next_bin)
                current = np.array([next_bin['lat'], next_bin['lon']])
                remaining.remove(next_bin)
            immediate_path = [self.warehouse] + [(b['lat'], b['lon']) for b in immediate_order] + [self.warehouse]
            folium.PolyLine(
                locations=immediate_path,
                color='black',
                weight=3,
                opacity=0.9,
                tooltip="Immediate Route"
            ).add_to(self.map)'''
           

       
        return self.map._repr_html_()

app = Flask(__name__)
classifier = WasteClassifier()

def generate_bins():
    center_lat, center_lon = 12.9716, 77.5946
    waste_types = ['Organic', 'Plastic', 'Metal', 'Paper', 'Mixed']
    bins = []
    for i in range(1, 101):
        bins.append({
            'id': i,
            'lat': center_lat + (random.random() - 0.5) * 0.1,
            'lon': center_lon + (random.random() - 0.5) * 0.1,
            'fill_level': random.randint(10, 95),
            'last_emptied': random.randint(1, 30),
            'waste_type': random.choice(waste_types)
        })
    return bins

bins = generate_bins()
def get_route_order(bins, warehouse):
    remaining = bins.copy()
    order = []
    current = np.array(warehouse)
    
    while remaining:
        next_bin = min(remaining, key=lambda b: np.linalg.norm(np.array([b['lat'], b['lon']]) - current))
        order.append(next_bin['id'])
        current = np.array([next_bin['lat'], next_bin['lon']])
        remaining.remove(next_bin)
    
    return order

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    
    prediction = None
    map_html = None
    
    try:
        if request.method == 'POST' and 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                image_path = os.path.join('static', 'upload.jpg')
                file.save(image_path)
                prediction = classifier.predict(image_path)
        
        optimizer = RouteOptimizer(bins)
        map_html = optimizer.optimize()
        avg_fill = round(sum(b['fill_level'] for b in bins) / len(bins), 1)
        urgent_bins = sum(1 for b in bins if b['fill_level'] > 80)
        urgent_bins_list = [b['id'] for b in bins if b['fill_level'] > 80]
        urgent_bins = len(urgent_bins_list)

        warehouse = (12.9716, 77.5946)
        route_order = get_route_order(bins, warehouse)
        

        
        return render_template('index.html',
                       prediction=prediction,
                       map_html=map_html,
                       avg_fill=avg_fill,
                       urgent_bins_count=urgent_bins,  
                       urgent_bins_list=urgent_bins_list,
                       route_order=route_order,  
                       update_time=datetime.now().strftime("%H:%M:%S"))


    
    except Exception as e:
        return f"Error loading dashboard: {str(e)}", 500

# HTML Template
app.jinja_env.globals.update(zip=zip)

@app.route('/template')
def template():
    return 

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(debug=True, port=5000)