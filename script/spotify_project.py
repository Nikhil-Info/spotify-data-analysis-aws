import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node album
album_node1740108227153 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotifyproject-s3/staging/albums.csv"]}, transformation_ctx="album_node1740108227153")

# Script generated for node track
track_node1740108227853 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotifyproject-s3/staging/track.csv"], "recurse": True}, transformation_ctx="track_node1740108227853")

# Script generated for node artist
artist_node1740108226537 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotifyproject-s3/staging/artists.csv"], "recurse": True}, transformation_ctx="artist_node1740108226537")

# Script generated for node Join album & artist
Joinalbumartist_node1740108350489 = Join.apply(frame1=album_node1740108227153, frame2=artist_node1740108226537, keys1=["artist_id"], keys2=["id"], transformation_ctx="Joinalbumartist_node1740108350489")

# Script generated for node Join with track
Joinwithtrack_node1740108610609 = Join.apply(frame1=track_node1740108227853, frame2=Joinalbumartist_node1740108350489, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Joinwithtrack_node1740108610609")

# Script generated for node Drop Fields
DropFields_node1740108703201 = DropFields.apply(frame=Joinwithtrack_node1740108610609, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1740108703201")

# Script generated for node Destination_s3
EvaluateDataQuality().process_rows(frame=DropFields_node1740108703201, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1740108033861", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Destination_s3_node1740108788856 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1740108703201, connection_type="s3", format="glueparquet", connection_options={"path": "s3://spotifyproject-s3/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_s3_node1740108788856")

job.commit()