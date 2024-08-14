# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:21:23 2024

@author: Xiao 

Script to plot 3D brain  made by Xiao
"""

import meshio
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns

# Import dataframe with points you want to plot
df_injection = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/PFC-STR project/str_tracing.csv', sep=';')

# 997: brain surface mesh
mesh = meshio.read("C:/Users/JoanaCatarino/.brainglobe/allen_mouse_10um_v1.2/meshes/997.obj")

v = mesh.points # vertices

### vn is not supported with plotly Mesh3D
# vn = mesh.point_data['obj:vn'] # vertice normal : The vn [i j k] Construct defines the vertex normal statement. Vertex normals are used to smooth a polygon surface (by lighting calculations). Vertex normals affect the smooth shading and rendering of geometry. A vertex normal statement begins with the characters "vn" and is followed by three floating-point values that define the normal vector.

#Plot layout of the brain in light gray
f = mesh.cells[0].data

fig = go.Figure(go.Mesh3d(x=v.T[0],y=v.T[1],z=v.T[2],
                          i=f.T[0],j=f.T[1],k=f.T[2],
                          opacity=0.2,
                          color='#DFE1DF'))

fig.update_layout(scene = dict(
        xaxis = dict(visible=False),
        yaxis = dict(visible=False),
        zaxis =dict(visible=False)))
  

#Plot layout of the area of interest
mesh_str = meshio.read("C:/Users/JoanaCatarino/.brainglobe/allen_mouse_10um_v1.2/meshes/477.obj") # Striatum

v_str = mesh_str.points
f_str = mesh_str.cells[0].data

fig.add_mesh3d(x=v_str.T[0],y=v_str.T[1],z=v_str.T[2],
               i=f_str.T[0],j=f_str.T[1],k=f_str.T[2],color='#C6D7F5',opacity=0.7)


# Plot injection coordinates within the region of interest 
    #In this case we want to plot the injection targets

# Set variables for injections targets (we are using 3 slices with 4 injections in each)
start_dms = df_injection[(df_injection.slice == 'start') & (df_injection.region == 'DMS')]
start_dls = df_injection[(df_injection.slice == 'start') & (df_injection.region == 'DLS')]
start_vms = df_injection[(df_injection.slice == 'start') & (df_injection.region == 'VMS')]
start_vls = df_injection[(df_injection.slice == 'start') & (df_injection.region == 'VLS')]
middle_dms = df_injection[(df_injection.slice == 'middle') & (df_injection.region == 'DMS')]
middle_dls = df_injection[(df_injection.slice == 'middle') & (df_injection.region == 'DLS')]
middle_vms = df_injection[(df_injection.slice == 'middle') & (df_injection.region == 'VMS')]
middle_vls = df_injection[(df_injection.slice == 'middle') & (df_injection.region == 'VLS')]
end_dms = df_injection[(df_injection.slice == 'end') & (df_injection.region == 'DMS')]
end_dls = df_injection[(df_injection.slice == 'end') & (df_injection.region == 'DLS')]
end_vms = df_injection[(df_injection.slice == 'end') & (df_injection.region == 'VMS')]
end_vls = df_injection[(df_injection.slice == 'end') & (df_injection.region == 'VLS')]

# Plot a data point for each coordinate within the striatum 

fig.add_scatter3d(x=start_dms["AP"].values.T*10, 
                  y=start_dms["DV"].values.T*10, 
                  z=start_dms["ML"].values.T*10,
                  mode='markers',
                  marker=dict(size=3,
                              color="rgb(255,0,0)",   # choose a colorscale
                              opacity=1),
                              name="middle",
                              hovertext=df_injection["region"].values,
                              hoverinfo="text")


fig.add_scatter3d(x=df_aldh["ap_coords"].values.T*10, 
                  y=df_aldh["dv_coords"].values.T*10, 
                  z=df_aldh["ml_coords"].values.T*10,
                  mode='markers',
        marker=dict(
        size=3,
        color="rgb(0,255,0)",   # choose a colorscale
        opacity=1),
        name="Aldh1a1",
        hovertext=df_aldh["name"].values,
        hoverinfo="text"
        )

fig.add_scatter3d(x=df_th["ap_coords"].values.T*10, 
                  y=df_th["dv_coords"].values.T*10, 
                  z=df_th["ml_coords"].values.T*10,
                  mode='markers',
        marker=dict(
        size=3,
        color="rgb(0,0,255)",   # choose a colorscale
        opacity=1),
        name="TH",
        hovertext=df_aldh["name"].values,
        hoverinfo="text"
        )


fig.write_html('clean_results.html', auto_open=True)