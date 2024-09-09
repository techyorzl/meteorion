import cdsapi

dataset = "reanalysis-era5-single-levels"
request = {
    'product_type': ['reanalysis'],
    'variable': ['10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature', '2m_temperature', 'mean_sea_level_pressure', 'sea_surface_temperature', 'significant_height_of_combined_wind_waves_and_swell', 'surface_pressure', 'total_precipitation', 'surface_latent_heat_flux', 'surface_sensible_heat_flux', 'surface_thermal_radiation_downwards', 'total_cloud_cover', 'volumetric_soil_water_layer_1', 'vertical_integral_of_divergence_of_moisture_flux', 'boundary_layer_height', 'convective_available_potential_energy', 'geopotential', 'total_column_ozone', 'total_column_water_vapour'],
    'year': ['2010'],
    'month': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
    'day': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
    'time': ['00:00', '06:00', '12:00', '18:00'],
    'data_format': 'grib',
    'download_format': 'unarchived',
    'area': [60, -60, 45, 165]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()
