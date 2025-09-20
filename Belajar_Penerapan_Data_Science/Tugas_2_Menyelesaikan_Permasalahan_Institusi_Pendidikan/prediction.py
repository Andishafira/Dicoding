import joblib

relative_path = './Belajar_Penerapan_Data_Science/Tugas_2_Menyelesaikan_Permasalahan_Institusi_Pendidikan/'

model = joblib.load(relative_path + "model/rdf_model.joblib")
result_target = joblib.load(relative_path + "model/status_encoder.joblib")

def prediction(data):
    result = model.predict(data)
    final_result = result_target.inverse_transform(result)[0]
    return final_result
