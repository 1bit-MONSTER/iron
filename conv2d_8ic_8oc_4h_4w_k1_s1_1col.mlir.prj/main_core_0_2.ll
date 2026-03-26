; ModuleID = 'LLVMDialectModule'
source_filename = "LLVMDialectModule"
target triple = "aie2p"

@_anonymous0 = external global [3 x i32]
@in_0_cons_buff_1 = external global [32 x bfloat]
@in_0_cons_buff_0 = external global [32 x bfloat]
@out_0_buff_1 = external global [32 x bfloat]
@out_0_buff_0 = external global [32 x bfloat]
@wt_0_cons_buff_0 = external global [64 x bfloat]

declare void @debug_i32(i32)

; Unknown intrinsic
declare void @llvm.aie2p.event(i32)

; Unknown intrinsic
declare void @llvm.aie2p.put.ms(i32, i32)

; Unknown intrinsic
declare { i32, i32 } @llvm.aie2p.get.ss()

; Unknown intrinsic
declare void @llvm.aie2p.mcd.write.vec(<16 x i32>, i32)

; Unknown intrinsic
declare <16 x i32> @llvm.aie2p.scd.read.vec(i32)

; Unknown intrinsic
declare void @llvm.aie2p.acquire(i32, i32)

; Unknown intrinsic
declare void @llvm.aie2p.release(i32, i32)

; Unknown intrinsic
declare void @llvm.aie2p.set.ctrl.reg(i32, i32)

declare void @conv2dk1_bf16(ptr, ptr, ptr, i32, i32, i32)

define void @core_0_2() {
  store i32 0, ptr @_anonymous0, align 4
  store i32 0, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i64 4), align 4
  store i32 0, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i64 8), align 4
  br label %1

1:                                                ; preds = %30, %0
  %2 = phi i64 [ %35, %30 ], [ 0, %0 ]
  %3 = icmp slt i64 %2, 9223372036854775807
  br i1 %3, label %4, label %36

4:                                                ; preds = %1
  call void @llvm.aie2p.acquire(i32 53, i32 -1)
  br label %5

5:                                                ; preds = %18, %4
  %6 = phi i64 [ %29, %18 ], [ 0, %4 ]
  %7 = icmp slt i64 %6, 4
  br i1 %7, label %8, label %30

8:                                                ; preds = %5
  call void @llvm.aie2p.acquire(i32 49, i32 -1)
  %9 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i64 4), align 4
  switch i32 %9, label %10 [
    i32 0, label %37
    i32 1, label %39
  ]

10:                                               ; preds = %37, %39, %8
  %11 = phi ptr [ %40, %39 ], [ %38, %37 ], [ @in_0_cons_buff_0, %8 ]
  %12 = getelementptr [32 x bfloat], ptr %11, i32 0, i32 0
  br label %13

13:                                               ; preds = %10
  call void @llvm.aie2p.acquire(i32 50, i32 -1)
  %14 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i64 8), align 4
  switch i32 %14, label %15 [
    i32 0, label %41
    i32 1, label %43
  ]

15:                                               ; preds = %41, %43, %13
  %16 = phi ptr [ %44, %43 ], [ %42, %41 ], [ @out_0_buff_0, %13 ]
  %17 = getelementptr [32 x bfloat], ptr %16, i32 0, i32 0
  br label %18

18:                                               ; preds = %15
  call void @conv2dk1_bf16(ptr %12, ptr @wt_0_cons_buff_0, ptr %17, i32 4, i32 8, i32 8)
  call void @llvm.aie2p.release(i32 48, i32 1)
  %19 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i64 4), align 4
  %20 = add i32 %19, 1
  %21 = icmp sge i32 %20, 2
  %22 = add i32 %19, -1
  %23 = select i1 %21, i32 %22, i32 %20
  store i32 %23, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i64 4), align 4
  call void @llvm.aie2p.release(i32 51, i32 1)
  %24 = load i32, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i64 8), align 4
  %25 = add i32 %24, 1
  %26 = icmp sge i32 %25, 2
  %27 = add i32 %24, -1
  %28 = select i1 %26, i32 %27, i32 %25
  store i32 %28, ptr getelementptr inbounds nuw (i8, ptr @_anonymous0, i64 8), align 4
  %29 = add i64 %6, 1
  br label %5

30:                                               ; preds = %5
  call void @llvm.aie2p.release(i32 52, i32 1)
  %31 = load i32, ptr @_anonymous0, align 4
  %32 = add i32 %31, 1
  %33 = icmp sge i32 %32, 1
  %34 = select i1 %33, i32 %31, i32 %32
  store i32 %34, ptr @_anonymous0, align 4
  %35 = add i64 %2, 1
  br label %1

36:                                               ; preds = %1
  ret void

37:                                               ; preds = %8
  %38 = phi ptr [ @in_0_cons_buff_0, %8 ]
  br label %10

39:                                               ; preds = %8
  %40 = phi ptr [ @in_0_cons_buff_1, %8 ]
  br label %10

41:                                               ; preds = %13
  %42 = phi ptr [ @out_0_buff_0, %13 ]
  br label %15

43:                                               ; preds = %13
  %44 = phi ptr [ @out_0_buff_1, %13 ]
  br label %15
}

!llvm.module.flags = !{!0}

!0 = !{i32 2, !"Debug Info Version", i32 3}
