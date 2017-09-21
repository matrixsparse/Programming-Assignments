import gulp from 'gulp';
import gulpif from 'gulp-if';
import concat from 'gulp-concat';
import webpack from 'webpack';
import gulpWebpack from 'webpack-stream';
import named from 'vinyl-named';
import livereload from 'gulp-livereload';
import plumber from 'gulp-plumber';
import rename from 'gulp-rename';
import uglify from 'gulp-uglify';
import {log,colors} from 'gulp-util';
import args from './util/args'

gulp.task('scripts',()=>{
  return gulp.src(['app/js/index.js'])
    .pipe(plumber({
      errorHandle:function(){

      }
    }))
    .pipe(named())
    .pipe(gulpWebpack({
      module:{
        loaders:[{
          test:/\.js$/,
          loader:'babel'
        }]
      }
    }),null,(err,states)=>{
      log(`Finished${colors.cyan('scripts')}`,states.toString({
        chunks:false
      }))
    })
    .pipe(gulp.dest('server/public/js'))
    // 编译压缩
    .pipe(rename({
      basename:'cp',
      extname:'.min.js'
    }))
    // 配置怎么压缩
    .pipe(uglify({compress:{properties:false},output:{'quote_keys':true}}))
    // 设置存储文件路径
    .pipe(gulp.dest('server/public/js'))
    // 监听文件，文件变化后自动更新，文件热更新
    .pipe(gulpif(args.watch.livereload()))
})
