from flask import Flask, render_template
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    # Create a sample data frame
    data = {
        'Category':['A', 'B', 'C', 'D', 'E'],
        'Value': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)

    # Create a bar char using Plotly
    fig = px.bar(df, x='Category', y='Value', title='Sample Bar Chart')

    # Render the HTML template with the visualization
    return render_template('index.html',plot = fig)

if __name__ == '__main__':
    app.run(debug=False)
