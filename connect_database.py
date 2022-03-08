from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
def get_data():
    cloud_config= {'secure_connect_bundle': 'secure-connect-ineuron.zip'}
    auth_provider = PlainTextAuthProvider('mkITgbJhSQokpgmXnFlbJOoF', '0k,p6Y1Iwxu2nYYnmhBUYwZs-PSmhc0lhm64-PnvqN414h7z9eRJrcawGnrxF08Q5KahaWPQlp.cptUdtdi7wcJu_Aek05vp3qZTEQW7XBOoh,t-4_EILBO2kZ3PhRyN')
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    return session.execute("select * from flights.flights")