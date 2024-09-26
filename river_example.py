from river.anomaly import OneClassSVM

anomaly_detector = OneClassSVM()

anomaly_detector.learn_one({'feature1': 1, 'feature2': 2})

anomaly_score = anomaly_detector.score_one({'feature1': 3, 'feature2': 4})
print(anomaly_score)