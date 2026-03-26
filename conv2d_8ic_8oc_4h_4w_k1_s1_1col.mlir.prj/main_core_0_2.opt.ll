; ModuleID = 'conv2d_8ic_8oc_4h_4w_k1_s1_1col.mlir.prj/main_core_0_2.ll'
source_filename = "LLVMDialectModule"
target datalayout = "e-m:e-p:20:32-i1:8:32-i8:8:32-i16:16:32-i32:32:32-f32:32:32-i64:32-f64:32-a:0:32-n32"
target triple = "aie2p"

@_anonymous0 = external local_unnamed_addr global [3 x i32]
@in_0_cons_buff_1 = external global [32 x bfloat]
@in_0_cons_buff_0 = external global [32 x bfloat]
@out_0_buff_1 = external global [32 x bfloat]
@out_0_buff_0 = external global [32 x bfloat]
@wt_0_cons_buff_0 = external global [64 x bfloat]

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn
declare void @llvm.aie2p.acquire(i32, i32) #0

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn
declare void @llvm.aie2p.release(i32, i32) #0

declare void @conv2dk1_bf16(ptr, ptr, ptr, i32, i32, i32) local_unnamed_addr

define void @core_0_2() local_unnamed_addr {
  store i32 0, ptr @_anonymous0, align 4
  store i32 0, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  store i32 0, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  br label %1

1:                                                ; preds = %0, %1
  %2 = phi i64 [ 0, %0 ], [ %71, %1 ]
  tail call void @llvm.aie2p.acquire(i32 53, i32 -1)
  tail call void @llvm.aie2p.acquire(i32 49, i32 -1)
  %3 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  %4 = icmp eq i32 %3, 1
  %5 = select i1 %4, ptr @in_0_cons_buff_1, ptr @in_0_cons_buff_0
  tail call void @llvm.aie2p.acquire(i32 50, i32 -1)
  %6 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  %7 = icmp eq i32 %6, 1
  %8 = select i1 %7, ptr @out_0_buff_1, ptr @out_0_buff_0
  tail call void @conv2dk1_bf16(ptr nonnull %5, ptr nonnull @wt_0_cons_buff_0, ptr nonnull %8, i32 4, i32 8, i32 8)
  tail call void @llvm.aie2p.release(i32 48, i32 1)
  %9 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  %10 = add i32 %9, 1
  %11 = icmp sgt i32 %10, 1
  %12 = add i32 %9, -1
  %13 = select i1 %11, i32 %12, i32 %10
  store i32 %13, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  tail call void @llvm.aie2p.release(i32 51, i32 1)
  %14 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  %15 = add i32 %14, 1
  %16 = icmp sgt i32 %15, 1
  %17 = add i32 %14, -1
  %18 = select i1 %16, i32 %17, i32 %15
  store i32 %18, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  tail call void @llvm.aie2p.acquire(i32 49, i32 -1)
  %19 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  %20 = icmp eq i32 %19, 1
  %21 = select i1 %20, ptr @in_0_cons_buff_1, ptr @in_0_cons_buff_0
  tail call void @llvm.aie2p.acquire(i32 50, i32 -1)
  %22 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  %23 = icmp eq i32 %22, 1
  %24 = select i1 %23, ptr @out_0_buff_1, ptr @out_0_buff_0
  tail call void @conv2dk1_bf16(ptr nonnull %21, ptr nonnull @wt_0_cons_buff_0, ptr nonnull %24, i32 4, i32 8, i32 8)
  tail call void @llvm.aie2p.release(i32 48, i32 1)
  %25 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  %26 = add i32 %25, 1
  %27 = icmp sgt i32 %26, 1
  %28 = add i32 %25, -1
  %29 = select i1 %27, i32 %28, i32 %26
  store i32 %29, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  tail call void @llvm.aie2p.release(i32 51, i32 1)
  %30 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  %31 = add i32 %30, 1
  %32 = icmp sgt i32 %31, 1
  %33 = add i32 %30, -1
  %34 = select i1 %32, i32 %33, i32 %31
  store i32 %34, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  tail call void @llvm.aie2p.acquire(i32 49, i32 -1)
  %35 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  %36 = icmp eq i32 %35, 1
  %37 = select i1 %36, ptr @in_0_cons_buff_1, ptr @in_0_cons_buff_0
  tail call void @llvm.aie2p.acquire(i32 50, i32 -1)
  %38 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  %39 = icmp eq i32 %38, 1
  %40 = select i1 %39, ptr @out_0_buff_1, ptr @out_0_buff_0
  tail call void @conv2dk1_bf16(ptr nonnull %37, ptr nonnull @wt_0_cons_buff_0, ptr nonnull %40, i32 4, i32 8, i32 8)
  tail call void @llvm.aie2p.release(i32 48, i32 1)
  %41 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  %42 = add i32 %41, 1
  %43 = icmp sgt i32 %42, 1
  %44 = add i32 %41, -1
  %45 = select i1 %43, i32 %44, i32 %42
  store i32 %45, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  tail call void @llvm.aie2p.release(i32 51, i32 1)
  %46 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  %47 = add i32 %46, 1
  %48 = icmp sgt i32 %47, 1
  %49 = add i32 %46, -1
  %50 = select i1 %48, i32 %49, i32 %47
  store i32 %50, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  tail call void @llvm.aie2p.acquire(i32 49, i32 -1)
  %51 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  %52 = icmp eq i32 %51, 1
  %53 = select i1 %52, ptr @in_0_cons_buff_1, ptr @in_0_cons_buff_0
  tail call void @llvm.aie2p.acquire(i32 50, i32 -1)
  %54 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  %55 = icmp eq i32 %54, 1
  %56 = select i1 %55, ptr @out_0_buff_1, ptr @out_0_buff_0
  tail call void @conv2dk1_bf16(ptr nonnull %53, ptr nonnull @wt_0_cons_buff_0, ptr nonnull %56, i32 4, i32 8, i32 8)
  tail call void @llvm.aie2p.release(i32 48, i32 1)
  %57 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  %58 = add i32 %57, 1
  %59 = icmp sgt i32 %58, 1
  %60 = add i32 %57, -1
  %61 = select i1 %59, i32 %60, i32 %58
  store i32 %61, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 4), align 4
  tail call void @llvm.aie2p.release(i32 51, i32 1)
  %62 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  %63 = add i32 %62, 1
  %64 = icmp sgt i32 %63, 1
  %65 = add i32 %62, -1
  %66 = select i1 %64, i32 %65, i32 %63
  store i32 %66, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i20 8), align 4
  tail call void @llvm.aie2p.release(i32 52, i32 1)
  %67 = load i32, ptr @_anonymous0, align 4
  %68 = icmp ugt i32 %67, 2147483646
  %69 = zext i1 %68 to i32
  %70 = add i32 %67, %69
  store i32 %70, ptr @_anonymous0, align 4
  %71 = add nuw nsw i64 %2, 1
  %72 = icmp eq i64 %71, 9223372036854775807
  br i1 %72, label %73, label %1

73:                                               ; preds = %1
  ret void
}

attributes #0 = { mustprogress nocallback nofree nosync nounwind willreturn }

!llvm.module.flags = !{!0}

!0 = !{i32 2, !"Debug Info Version", i32 3}
