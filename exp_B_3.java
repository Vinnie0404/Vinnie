import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class SimpleWeather {

    // 🔹 Mapper
    public static class Map extends Mapper<Object, Text, Text, IntWritable> {

        public void map(Object key, Text value, Context context)
                throws IOException, InterruptedException {

            String[] data = value.toString().split(",");

            if (data.length == 2) {
                context.write(new Text(data[0]), new IntWritable(Integer.parseInt(data[1])));
            }
        }
    }

    // 🔹 Reducer
    public static class Reduce extends Reducer<Text, IntWritable, Text, Text> {

        public void reduce(Text key, Iterable<IntWritable> values, Context context)
                throws IOException, InterruptedException {

            int sum = 0, count = 0;
            int max = Integer.MIN_VALUE;
            int min = Integer.MAX_VALUE;

            for (IntWritable val : values) {
                int temp = val.get();

                sum += temp;
                count++;

                if (temp > max) max = temp;
                if (temp < min) min = temp;
            }

            double avg = (double) sum / count;

            context.write(key, new Text(
                "Max=" + max + " Min=" + min + " Avg=" + avg
            ));
        }
    }

    // 🔹 Driver
    public static void main(String[] args) throws Exception {

        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Simple Weather");

        job.setJarByClass(SimpleWeather.class);
        job.setMapperClass(Map.class);
        job.setReducerClass(Reduce.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        job.waitForCompletion(true);
    }
}
