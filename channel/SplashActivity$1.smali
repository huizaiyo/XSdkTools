.class Lcom/haowan/funcell/sdk/api/splash/SplashActivity$1;
.super Ljava/lang/Object;
.source "SplashActivity.java"

# interfaces
.implements Landroid/view/animation/Animation$AnimationListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->appendAnimation()V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/haowan/funcell/sdk/api/splash/SplashActivity;


# direct methods
.method constructor <init>(Lcom/haowan/funcell/sdk/api/splash/SplashActivity;)V
    .locals 0

    .prologue
    .line 1
    iput-object p1, p0, Lcom/haowan/funcell/sdk/api/splash/SplashActivity$1;->this$0:Lcom/haowan/funcell/sdk/api/splash/SplashActivity;

    .line 50
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onAnimationEnd(Landroid/view/animation/Animation;)V
    .locals 1
    .param p1, "animation"    # Landroid/view/animation/Animation;

    .prologue
    .line 66
    iget-object v0, p0, Lcom/haowan/funcell/sdk/api/splash/SplashActivity$1;->this$0:Lcom/haowan/funcell/sdk/api/splash/SplashActivity;

    # invokes: Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->startGameActivity()V
    invoke-static {v0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->access$0(Lcom/haowan/funcell/sdk/api/splash/SplashActivity;)V

    .line 67
    return-void
.end method

.method public onAnimationRepeat(Landroid/view/animation/Animation;)V
    .locals 0
    .param p1, "animation"    # Landroid/view/animation/Animation;

    .prologue
    .line 62
    return-void
.end method

.method public onAnimationStart(Landroid/view/animation/Animation;)V
    .locals 0
    .param p1, "animation"    # Landroid/view/animation/Animation;

    .prologue
    .line 56
    return-void
.end method
