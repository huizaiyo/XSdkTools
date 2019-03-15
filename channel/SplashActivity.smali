.class public Lcom/haowan/funcell/sdk/api/splash/SplashActivity;
.super Landroid/app/Activity;
.source "SplashActivity.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 19
    invoke-direct {p0}, Landroid/app/Activity;-><init>()V

    return-void
.end method

.method static synthetic access$0(Lcom/haowan/funcell/sdk/api/splash/SplashActivity;)V
    .locals 0

    .prologue
    .line 71
    invoke-direct {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->startGameActivity()V

    return-void
.end method

.method private appendAnimation()V
    .locals 14

    .prologue
    const/4 v13, 0x0

    .line 30
    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->getResources()Landroid/content/res/Resources;

    move-result-object v5

    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    const-string v9, "funcell_splash_time"

    const-string v10, "string"

    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->getPackageName()Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v8, v9, v10, v11}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v8

    invoke-virtual {v5, v8}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-static {v5}, Ljava/lang/Long;->valueOf(Ljava/lang/String;)Ljava/lang/Long;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/Long;->longValue()J

    move-result-wide v6

    .line 31
    .local v6, "time":J
    new-instance v5, Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->getResources()Landroid/content/res/Resources;

    move-result-object v9

    const-string v10, "funcell_splash_fromAlpha"

    const-string v11, "string"

    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->getPackageName()Ljava/lang/String;

    move-result-object v12

    invoke-virtual {v9, v10, v11, v12}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v9

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v8

    invoke-static {v8}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v8

    invoke-direct {v5, v8}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    const-string v8, "f"

    invoke-virtual {v5, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v5}, Ljava/lang/Float;->valueOf(Ljava/lang/String;)Ljava/lang/Float;

    move-result-object v2

    .line 32
    .local v2, "fromAlpha":Ljava/lang/Float;
    const-string v5, "SplashActivity"

    new-instance v8, Ljava/lang/StringBuilder;

    const-string v9, "time:"

    invoke-direct {v8, v9}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    invoke-virtual {v8, v6, v7}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    move-result-object v8

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-static {v5, v8}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 33
    const-string v5, "SplashActivity"

    new-instance v8, Ljava/lang/StringBuilder;

    const-string v9, "fromAlpha:"

    invoke-direct {v8, v9}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    invoke-virtual {v8, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v8

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-static {v5, v8}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 34
    new-instance v0, Landroid/view/animation/AlphaAnimation;

    invoke-virtual {v2}, Ljava/lang/Float;->floatValue()F

    move-result v5

    const/high16 v8, 0x3f800000    # 1.0f

    invoke-direct {v0, v5, v8}, Landroid/view/animation/AlphaAnimation;-><init>(FF)V

    .line 35
    .local v0, "ani":Landroid/view/animation/AlphaAnimation;
    const/4 v5, 0x2

    invoke-virtual {v0, v5}, Landroid/view/animation/AlphaAnimation;->setRepeatMode(I)V

    .line 36
    invoke-virtual {v0, v13}, Landroid/view/animation/AlphaAnimation;->setRepeatCount(I)V

    .line 37
    invoke-virtual {v0, v6, v7}, Landroid/view/animation/AlphaAnimation;->setDuration(J)V

    .line 38
    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->getResources()Landroid/content/res/Resources;

    move-result-object v5

    const-string v8, "fun_plugin_splash_img"

    const-string v9, "id"

    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->getPackageName()Ljava/lang/String;

    move-result-object v10

    invoke-virtual {v5, v8, v9, v10}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v5

    invoke-virtual {p0, v5}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->findViewById(I)Landroid/view/View;

    move-result-object v3

    check-cast v3, Landroid/widget/ImageView;

    .line 40
    .local v3, "image":Landroid/widget/ImageView;
    if-nez v3, :cond_0

    .line 41
    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->getResources()Landroid/content/res/Resources;

    move-result-object v5

    const-string v8, "fun_plugin_splash_layout"

    const-string v9, "id"

    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->getPackageName()Ljava/lang/String;

    move-result-object v10

    invoke-virtual {v5, v8, v9, v10}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v1

    .line 42
    .local v1, "defaultID":I
    invoke-static {p0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v5

    const/4 v8, 0x0

    invoke-virtual {v5, v1, v8}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v4

    check-cast v4, Landroid/widget/RelativeLayout;

    .line 43
    .local v4, "layout":Landroid/widget/RelativeLayout;
    invoke-virtual {v4, v13}, Landroid/widget/RelativeLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v3

    .end local v3    # "image":Landroid/widget/ImageView;
    check-cast v3, Landroid/widget/ImageView;

    .line 49
    .end local v1    # "defaultID":I
    .end local v4    # "layout":Landroid/widget/RelativeLayout;
    .restart local v3    # "image":Landroid/widget/ImageView;
    :cond_0
    invoke-virtual {v3, v0}, Landroid/widget/ImageView;->setAnimation(Landroid/view/animation/Animation;)V

    .line 50
    new-instance v5, Lcom/haowan/funcell/sdk/api/splash/SplashActivity$1;

    invoke-direct {v5, p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity$1;-><init>(Lcom/haowan/funcell/sdk/api/splash/SplashActivity;)V

    invoke-virtual {v0, v5}, Landroid/view/animation/AlphaAnimation;->setAnimationListener(Landroid/view/animation/Animation$AnimationListener;)V

    .line 69
    return-void
.end method

.method private startGameActivity()V
    .locals 4

    .prologue
    .line 73
    :try_start_0
    const-string v3, "###FuncellSdk_Start_Activity###"

    invoke-static {v3}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v2

    .line 74
    .local v2, "mainClass":Ljava/lang/Class;, "Ljava/lang/Class<*>;"
    new-instance v1, Landroid/content/Intent;

    invoke-direct {v1, p0, v2}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    .line 75
    .local v1, "intent":Landroid/content/Intent;
    invoke-virtual {p0, v1}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->startActivity(Landroid/content/Intent;)V

    .line 76
    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->finish()V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    .line 81
    .end local v1    # "intent":Landroid/content/Intent;
    .end local v2    # "mainClass":Ljava/lang/Class;, "Ljava/lang/Class<*>;"
    :goto_0
    return-void

    .line 78
    :catch_0
    move-exception v0

    .line 79
    .local v0, "e":Ljava/lang/Exception;
    invoke-virtual {v0}, Ljava/lang/Exception;->printStackTrace()V

    goto :goto_0
.end method


# virtual methods
.method public onCreate(Landroid/os/Bundle;)V
    .locals 5
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .prologue
    .line 23
    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V

    .line 24
    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    const-string v2, "funcell_plugin_splash"

    const-string v3, "layout"

    invoke-virtual {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->getPackageName()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v1, v2, v3, v4}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v0

    .line 25
    .local v0, "layoutID":I
    invoke-virtual {p0, v0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->setContentView(I)V

    .line 26
    invoke-direct {p0}, Lcom/haowan/funcell/sdk/api/splash/SplashActivity;->appendAnimation()V

    .line 27
    return-void
.end method
