from fastapi import FastAPI
from routers import user_router, personal_info_router, education_router, degree_router, online_course_router, certification_router, highSchool_router, thesis_router, keyword_mapping_router, keyword_router, course_router, completedCourse_router
from routers import internship_router, project_router, skillValidatedMapping_router, skillValidated_router


app = FastAPI()

app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(personal_info_router.router, prefix="/personalInfo", tags=["PersonalInfo"])
app.include_router(education_router.router, prefix="/education", tags=["Education"])
app.include_router(degree_router.router, prefix="/degree", tags=["Degree"])
app.include_router(online_course_router.router, prefix="/onlineCourse", tags=["Online Course"])
app.include_router(certification_router.router, prefix="/certification", tags=["Certification"])
app.include_router(highSchool_router.router, prefix="/highSchool", tags=["High School"])
app.include_router(thesis_router.router, prefix="/thesis", tags=["Thesis"])
app.include_router(keyword_mapping_router.router, prefix="/keywordMapping", tags=["Keyword Mapping"])
app.include_router(keyword_router.router, prefix="/keyword", tags=["Keyword"])
app.include_router(course_router.router, prefix="/course", tags=["Course"])
app.include_router(completedCourse_router.router, prefix="/completedCourse", tags=["Completed Course"])
app.include_router(internship_router.router, prefix="/internship", tags=["Internship"])
app.include_router(project_router.router, prefix="/project", tags=["Project"])
app.include_router(skillValidatedMapping_router.router, prefix="/skillValidatedMapping", tags=["Skill Validated Mapping"])
app.include_router(skillValidated_router.router, prefix="/skillValidated", tags=["Skill Validated"])