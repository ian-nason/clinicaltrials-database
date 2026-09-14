# Data Dictionary

Source: [AACT (Aggregate Analysis of ClinicalTrials.gov)](https://aact.ctti-clinicaltrials.org/)

## baseline_counts

Sample sizes at baseline for each study group

Source file: `baseline_counts.txt`
Rows: 240,449

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count | BIGINT | 0.0% | 201 |  |
| scope | VARCHAR | 0.0% | overall |  |
| units | VARCHAR | 0.0% | Participants |  |
| ctgov_group_code | VARCHAR | 0.0% | BG000 |  |
| result_group_id | BIGINT | 0.0% | 854829238 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT01772147 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 95087922 | Table primary key (auto-increment) |

## baseline_measurements

Demographic and baseline measures by group

Source file: `baseline_measurements.txt`
Rows: 2,963,066

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| calculate_percentage | BOOLEAN | 96.5% | false |  |
| population_description | VARCHAR | 94.2% | All participants who received at least one dose of the investigational drug |  |
| number_analyzed_units | VARCHAR | 0.0% | Participants |  |
| number_analyzed | BIGINT | 0.1% | 201 |  |
| explanation_of_na | VARCHAR | 99.8% | Mean and standard deviation were not calculated for the total population as t... |  |
| dispersion_upper_limit | DOUBLE | 97.8% | 2.0 |  |
| dispersion_lower_limit | DOUBLE | 97.8% | 0.3 |  |
| dispersion_value_num | DOUBLE | 89.3% | 6.6 |  |
| dispersion_value | VARCHAR | 89.2% | 6.6 |  |
| dispersion_type | VARCHAR | 87.1% | STANDARD_DEVIATION |  |
| param_value_num | DOUBLE | 0.3% | 0.8 |  |
| param_value | VARCHAR | 0.1% | 0.8 |  |
| param_type | VARCHAR | 0.0% | MEDIAN |  |
| units | VARCHAR | 0.0% | percentage |  |
| description | VARCHAR | 90.2% | This data reflects data collected at the Baseline time point. Total bacteria ... |  |
| title | VARCHAR | 0.0% | Bifidobacterium spp. |  |
| category | VARCHAR | 35.5% | <=18 years |  |
| classification | VARCHAR | 74.5% | United States |  |
| ctgov_group_code | VARCHAR | 0.1% | BG000 |  |
| result_group_id | BIGINT | 0.1% | 854956500 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT00846053 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1112083998 | Table primary key (auto-increment) |

## brief_summaries

Brief text summary of the study protocol

Source file: `brief_summaries.txt`
Rows: 601,530

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 0.0% | Interventional, parallel groups, single center trial with a prospective design |  |
| nct_id | VARCHAR | 0.0% | NCT07376564 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 234119903 | Table primary key (auto-increment) |

## browse_conditions

NLM-generated MeSH terms for study conditions

Source file: `browse_conditions.txt`
Rows: 4,368,819

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| mesh_type | VARCHAR | 0.0% | mesh-ancestor |  |
| downcase_mesh_term | VARCHAR | 0.0% | rectal diseases |  |
| mesh_term | VARCHAR | 0.0% | Rectal Diseases |  |
| nct_id | VARCHAR | 0.0% | NCT02843217 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1653739095 | Table primary key (auto-increment) |

## browse_interventions

NLM-generated MeSH terms for study interventions

Source file: `browse_interventions.txt`
Rows: 2,553,067

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| mesh_type | VARCHAR | 0.0% | mesh-ancestor |  |
| downcase_mesh_term | VARCHAR | 0.0% | organic chemicals |  |
| mesh_term | VARCHAR | 0.0% | Taxoids |  |
| nct_id | VARCHAR | 0.0% | NCT00000294 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 867084090 | Table primary key (auto-increment) |

## calculated_values

AACT-computed fields: months to report results, facilities count, etc.

Source file: `calculated_values.txt`
Rows: 602,514

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| number_of_other_outcomes_to_measure | BIGINT | 91.4% | 4 |  |
| number_of_secondary_outcomes_to_measure | BIGINT | 27.3% | 4 |  |
| number_of_primary_outcomes_to_measure | BIGINT | 2.9% | 2 |  |
| maximum_age_unit | VARCHAR | 46.9% | year |  |
| minimum_age_unit | VARCHAR | 6.5% | year |  |
| maximum_age_num | BIGINT | 46.9% | 80 |  |
| minimum_age_num | BIGINT | 6.5% | 18 |  |
| has_single_facility | BOOLEAN | 10.0% | true |  |
| has_us_facility | BOOLEAN | 10.0% | false |  |
| months_to_report_results | BIGINT | 86.7% | 56 |  |
| were_results_reported | BOOLEAN | 0.0% | false |  |
| actual_duration | BIGINT | 38.7% | 101 |  |
| nlm_download_date | VARCHAR | 100.0% |  |  |
| registered_in_calendar_year | BIGINT | 0.0% | 2025 |  |
| number_of_sae_subjects | BIGINT | 92.9% | 9 |  |
| number_of_nsae_subjects | BIGINT | 90.9% | 6 |  |
| number_of_facilities | BIGINT | 0.0% | 1 |  |
| nct_id | VARCHAR | 0.0% | NCT06775340 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 257770602 | Table primary key (auto-increment) |

## central_contacts

Primary and backup contacts for enrollment questions

Source file: `central_contacts.txt`
Rows: 226,221

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| role | VARCHAR | 0.0% | CONTACT |  |
| phone_extension | VARCHAR | 88.5% | 1022 |  |
| email | VARCHAR | 2.3% | nikyli@clalit.org.il |  |
| phone | VARCHAR | 6.1% | (301) 480-3765 |  |
| name | VARCHAR | 0.0% | Dianna S Lovins |  |
| contact_type | VARCHAR | 0.0% | primary |  |
| nct_id | VARCHAR | 0.0% | NCT03685721 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 89621943 | Table primary key (auto-increment) |

## conditions

Disease or condition names studied in each trial

Source file: `conditions.txt`
Rows: 1,083,005

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| downcase_name | VARCHAR | 0.0% | sports physical therapy |  |
| name | VARCHAR | 0.0% | Sports Physical Therapy |  |
| nct_id | VARCHAR | 0.0% | NCT03884738 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 414375967 | Table primary key (auto-increment) |

## countries

Countries where the study has sites

Source file: `countries.txt`
Rows: 816,098

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| removed | BOOLEAN | 0.0% | true |  |
| name | VARCHAR | 0.0% | France |  |
| nct_id | VARCHAR | 0.0% | NCT03437733 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 322397195 | Table primary key (auto-increment) |

## design_group_interventions

Cross-reference mapping design groups to interventions

Source file: `design_group_interventions.txt`
Rows: 1,344,197

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| intervention_id | BIGINT | 0.0% | 397587581 | Joins to interventions.id |
| design_group_id | BIGINT | 0.0% | 443303736 | Joins to design_groups.id |
| nct_id | VARCHAR | 0.0% | NCT06062550 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 523924265 | Table primary key (auto-increment) |

## design_groups

Protocol-specified groups or cohorts assigned to interventions

Source file: `design_groups.txt`
Rows: 1,108,587

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 11.8% | Participants follow a Light Fasting diet during the first month, designed wit... |  |
| title | VARCHAR | 0.0% | Light fasting and Magnesium Supplementation |  |
| group_type | VARCHAR | 15.5% | EXPERIMENTAL |  |
| nct_id | VARCHAR | 0.0% | NCT07322120 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 442502717 | Table primary key (auto-increment) |

## design_outcomes

Planned outcome measures and observations

Source file: `design_outcomes.txt`
Rows: 3,761,914

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 17.4% | Patients will be imaged using diffusion-weighted MR. Findings will be correla... |  |
| population | VARCHAR | 100.0% |  |  |
| time_frame | VARCHAR | 1.4% | Approximately 6-9 months for MTD and RP2D (phase I duration) |  |
| measure | VARCHAR | 0.0% | Apparent Volume of Distribution (Vz/F) |  |
| outcome_type | VARCHAR | 0.0% | secondary |  |
| nct_id | VARCHAR | 0.0% | NCT04954001 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1445877698 | Table primary key (auto-increment) |

## designs

Study design details: allocation, masking, assignment, purpose

Source file: `designs.txt`
Rows: 597,720

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| outcomes_assessor_masked | BOOLEAN | 67.4% | true |  |
| investigator_masked | BOOLEAN | 67.4% | true |  |
| caregiver_masked | BOOLEAN | 67.4% | false |  |
| subject_masked | BOOLEAN | 67.4% | true |  |
| intervention_model_description | VARCHAR | 84.8% | Randomized 1:1:1 to two different ANAVEX2-73 doses or placebo |  |
| masking_description | VARCHAR | 92.2% | Masking Description |  |
| masking | VARCHAR | 24.0% | NONE |  |
| time_perspective | VARCHAR | 77.0% | PROSPECTIVE |  |
| primary_purpose | VARCHAR | 24.2% | TREATMENT |  |
| observational_model | VARCHAR | 77.4% | COHORT |  |
| intervention_model | VARCHAR | 24.2% | PARALLEL |  |
| allocation | VARCHAR | 24.0% | RANDOMIZED |  |
| nct_id | VARCHAR | 0.0% | NCT07406308 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 232447205 | Table primary key (auto-increment) |

## detailed_descriptions

Detailed text description of the study protocol

Source file: `detailed_descriptions.txt`
Rows: 601,530

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 32.8% | One of the goals in the Sustainable Development Goals (SDGs) is the availabil... |  |
| nct_id | VARCHAR | 0.0% | NCT06306859 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 234342203 | Table primary key (auto-increment) |

## documents

Full study protocol and statistical analysis plan

Source file: `documents.txt`
Rows: 10,838

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| comment | VARCHAR | 13.9% | For additional information about this study please refer to the GSK Clinical ... |  |
| url | VARCHAR | 0.0% | http://www.merck.com/clinical-trials/policies-perspectives.html |  |
| document_type | VARCHAR | 0.0% | CSR Synopsis |  |
| document_id | VARCHAR | 15.5% | 49653/048 | Joins to documents.id |
| nct_id | VARCHAR | 0.0% | NCT00202852 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 4477261 | Table primary key (auto-increment) |

## drop_withdrawals

Summary of participant withdrawals: counts and reasons

Source file: `drop_withdrawals.txt`
Rows: 602,414

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count_units | VARCHAR | 100.0% |  |  |
| reason_comment | VARCHAR | 100.0% |  |  |
| drop_withdraw_comment | VARCHAR | 100.0% |  |  |
| count | BIGINT | 0.0% | 0 |  |
| reason | VARCHAR | 0.0% | Did not receive Open-label BNT162b2 30 mcg |  |
| period | VARCHAR | 0.0% | Open-Label Period |  |
| ctgov_group_code | VARCHAR | 0.0% | FG026 |  |
| result_group_id | BIGINT | 0.0% | 856794869 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT04955626 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 233337365 | Table primary key (auto-increment) |

## eligibilities

Participant eligibility criteria (inclusion/exclusion, age, sex)

Source file: `eligibilities.txt`
Rows: 601,530

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| older_adult | BOOLEAN | 0.0% | false |  |
| child | BOOLEAN | 0.0% | true |  |
| adult | BOOLEAN | 0.0% | false |  |
| gender_based | BOOLEAN | 96.7% | true |  |
| gender_description | VARCHAR | 97.9% | Duchenne muscular dystrophy occurs mostly in boys and very rarely in girls. G... |  |
| criteria | VARCHAR | 0.0% | The study will consider mother-infant dyads eligible for participation if the... |  |
| population | VARCHAR | 77.3% | Subjects will be selected from kindergartens.Subjects will be divided into tw... |  |
| healthy_volunteers | BOOLEAN | 2.3% | true |  |
| maximum_age | VARCHAR | 46.8% | 6 Years |  |
| minimum_age | VARCHAR | 6.3% | 4 Years |  |
| gender | VARCHAR | 0.1% | ALL |  |
| sampling_method | VARCHAR | 77.3% | PROBABILITY_SAMPLE |  |
| nct_id | VARCHAR | 0.0% | NCT05948176 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 233974753 | Table primary key (auto-increment) |

## facilities

Facility names, addresses, and recruiting status

Source file: `facilities.txt`
Rows: 3,523,526

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| longitude | DOUBLE | 2.6% | -71.58979 |  |
| latitude | DOUBLE | 2.6% | 42.5612 |  |
| country | VARCHAR | 0.0% | United States |  |
| zip | VARCHAR | 19.1% | 01432 |  |
| state | VARCHAR | 39.1% | Massachusetts |  |
| city | VARCHAR | 0.0% | Ayer |  |
| name | VARCHAR | 6.2% | University of Colorado Anschutz Medical Campus |  |
| status | VARCHAR | 85.4% | RECRUITING |  |
| nct_id | VARCHAR | 0.0% | NCT05704361 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1423975155 | Table primary key (auto-increment) |

## facility_contacts

Contact information at each study facility

Source file: `facility_contacts.txt`
Rows: 421,325

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| phone_extension | VARCHAR | 94.4% | +33 |  |
| phone | VARCHAR | 27.6% | 86-18017312534 |  |
| email | VARCHAR | 27.7% | hsuroto2000@yahoo.com |  |
| name | VARCHAR | 3.3% | Heri Suroto, MD, PhD |  |
| contact_type | VARCHAR | 0.0% | primary |  |
| facility_id | BIGINT | 0.0% | 1424466638 | Joins to facilities.id |
| nct_id | VARCHAR | 0.0% | NCT04654286 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 178806662 | Table primary key (auto-increment) |

## facility_investigators

Investigator names at each study facility

Source file: `facility_investigators.txt`
Rows: 226,624

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | Luciana L Goncalves, Ph. D. |  |
| role | VARCHAR | 0.0% | PRINCIPAL_INVESTIGATOR |  |
| facility_id | BIGINT | 0.0% | 1426581109 | Joins to facilities.id |
| nct_id | VARCHAR | 0.0% | NCT07653464 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 96757031 | Table primary key (auto-increment) |

## id_information

Identifiers other than NCT ID (org study IDs, secondary IDs)

Source file: `id_information.txt`
Rows: 796,767

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| id_link | VARCHAR | 92.8% | https://reporter.nih.gov/quickSearch/2R01HL105495-06A1 |  |
| id_type_description | VARCHAR | 89.3% | New York State Psychiatric Institute Institutional Review Board |  |
| id_type | VARCHAR | 79.6% | NIH |  |
| id_value | VARCHAR | 0.0% | 9662 |  |
| id_source | VARCHAR | 0.0% | org_study_id |  |
| nct_id | VARCHAR | 0.0% | NCT07310940 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 305588629 | Table primary key (auto-increment) |

## intervention_other_names

Synonymous names for interventions

Source file: `intervention_other_names.txt`
Rows: 486,506

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | Fluoride Toothpaste / Crest® Cavity Protection Regular |  |
| intervention_id | BIGINT | 0.0% | 396880087 | Joins to interventions.id |
| nct_id | VARCHAR | 0.0% | NCT02113579 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 196969752 | Table primary key (auto-increment) |

## interventions

Interventions or exposures: drugs, devices, procedures, vaccines

Source file: `interventions.txt`
Rows: 1,019,126

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 9.0% | RC48 (2.5mg/kg iv on d1 , every 21d for 6 cycles) + Carboplatin (AUC5 iv on d... |  |
| name | VARCHAR | 0.0% | RC48+carboplatin±bevacizumab |  |
| intervention_type | VARCHAR | 0.0% | DRUG |  |
| nct_id | VARCHAR | 0.0% | NCT06420973 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 396914267 | Table primary key (auto-increment) |

## ipd_information_types

Individual participant data sharing information types

Source file: `ipd_information_types.txt`
Rows: 96,041

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | STUDY_PROTOCOL |  |
| nct_id | VARCHAR | 0.0% | NCT05288348 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 34163071 | Table primary key (auto-increment) |

## keywords

Investigator-provided keywords describing the study

Source file: `keywords.txt`
Rows: 1,621,092

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| downcase_name | VARCHAR | 0.0% | her-2 |  |
| name | VARCHAR | 0.0% | HER-2 |  |
| nct_id | VARCHAR | 0.0% | NCT01614522 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 615067834 | Table primary key (auto-increment) |

## links

Web links relevant to the study

Source file: `links.txt`
Rows: 75,845

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 0.0% | San Rocco Therapeutics |  |
| url | VARCHAR | 0.0% | https://sanroccotherapeutics.com/ |  |
| nct_id | VARCHAR | 0.0% | NCT01639690 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 30558110 | Table primary key (auto-increment) |

## milestones

Participant progress through each stage of the study

Source file: `milestones.txt`
Rows: 898,696

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count_units | BIGINT | 97.9% | 13 |  |
| milestone_description | VARCHAR | 96.5% | The 26-week extension was not required, and 4 patients elected to not start t... |  |
| count | BIGINT | 0.0% | 8 |  |
| description | VARCHAR | 100.0% | Overall Study |  |
| period | VARCHAR | 0.0% | Part 1 Immediate Effects tsDCS Higher |  |
| title | VARCHAR | 0.0% | COMPLETED |  |
| ctgov_group_code | VARCHAR | 0.0% | FG000 |  |
| result_group_id | BIGINT | 0.0% | 856845072 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT01751906 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 343484914 | Table primary key (auto-increment) |

## outcome_analyses

Statistical analyses performed on outcomes

Source file: `outcome_analyses.txt`
Rows: 326,441

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| p_value_raw | VARCHAR | 18.4% | 0.0156 |  |
| ci_lower_limit_raw | DOUBLE | 36.3% | 63.6 |  |
| ci_upper_limit_raw | VARCHAR | 36.4% | 75.1 |  |
| other_analysis_description | VARCHAR | 98.9% | For continuous outcomes, standard summary statistics will include n, mean, st... |  |
| groups_description | VARCHAR | 41.6% | Efficacy endpoints were analyzed using a Wilcoxon signed rank test on the pai... |  |
| estimate_description | VARCHAR | 78.2% | GMR and 90% confidence interval (CI) were estimated. Geometric Mean Ratio (GM... |  |
| method_description | VARCHAR | 81.0% | 2-sided |  |
| method | VARCHAR | 14.9% | Wilcoxon Signed rank |  |
| p_value_description | VARCHAR | 71.4% | Confidence intervals \[CI\] will be constructed for outcomes of interest at t... |  |
| ci_upper_limit_na_comment | VARCHAR | 100.0% | Not enough events |  |
| ci_upper_limit | DOUBLE | 36.4% | 75.1 |  |
| ci_lower_limit | DOUBLE | 36.3% | 63.6 |  |
| ci_percent | DOUBLE | 30.5% | 95.0 |  |
| ci_n_sides | VARCHAR | 32.6% | TWO_SIDED |  |
| p_value | DOUBLE | 18.4% | 0.003 |  |
| p_value_modifier | VARCHAR | 79.5% | < |  |
| dispersion_value | DOUBLE | 81.4% | 0.39 |  |
| dispersion_type | VARCHAR | 81.4% | STANDARD_ERROR_OF_MEAN |  |
| param_value | DOUBLE | 31.0% | 0.29 |  |
| param_type | VARCHAR | 31.0% | Kaplan-Meier |  |
| non_inferiority_description | VARCHAR | 85.7% | change from baseline |  |
| non_inferiority_type | VARCHAR | 0.0% | OTHER |  |
| outcome_id | BIGINT | 0.0% | 264045185 | Joins to outcomes.id |
| nct_id | VARCHAR | 0.0% | NCT00487942 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 131632152 | Table primary key (auto-increment) |

## outcome_analysis_groups

Groups involved in each outcome analysis

Source file: `outcome_analysis_groups.txt`
Rows: 631,153

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| result_group_id | BIGINT | 0.0% | 855637676 | Joins to result_groups.id |
| outcome_analysis_id | BIGINT | 0.0% | 131494392 | Joins to outcome_analyses.id |
| nct_id | VARCHAR | 0.0% | NCT04732221 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 254786835 | Table primary key (auto-increment) |

## outcome_counts

Sample sizes for each outcome by study group

Source file: `outcome_counts.txt`
Rows: 1,608,622

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count | BIGINT | 0.0% | 124 |  |
| units | VARCHAR | 0.0% | Participants |  |
| scope | VARCHAR | 0.0% | Measure |  |
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| result_group_id | BIGINT | 0.0% | 855296773 | Joins to result_groups.id |
| outcome_id | BIGINT | 0.0% | 263678610 | Joins to outcomes.id |
| nct_id | VARCHAR | 0.0% | NCT03170349 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 633501201 | Table primary key (auto-increment) |

## outcome_measurements

Summary data for outcome measures by study group

Source file: `outcome_measurements.txt`
Rows: 4,995,195

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| dispersion_lower_limit_raw | VARCHAR | 82.6% | 3.2 |  |
| dispersion_upper_limit_raw | VARCHAR | 82.7% | 23.2 |  |
| explanation_of_na | VARCHAR | 98.0% | No exacerbations occurred in this group |  |
| dispersion_upper_limit | DOUBLE | 83.4% | 23.2 |  |
| dispersion_lower_limit | DOUBLE | 83.0% | 12.8 |  |
| dispersion_value_num | DOUBLE | 64.8% | 12.8 |  |
| dispersion_value | VARCHAR | 63.7% | 12.8 |  |
| dispersion_type | VARCHAR | 46.7% | 95% Confidence Interval |  |
| param_value_num | DOUBLE | 1.1% | 0.0 |  |
| param_value | VARCHAR | 0.0% | 0 |  |
| param_type | VARCHAR | 0.0% | MEAN |  |
| units | VARCHAR | 0.0% | score on a scale |  |
| description | VARCHAR | 4.6% | Tissue was collected for VEGF, VEGRfR2 and HER2 at baseline. Patients underwe... |  |
| title | VARCHAR | 0.0% | Levels of VEGF, VEGRfR2 and HER2 Expression in Tumor Tissue as Compared to Re... |  |
| category | VARCHAR | 93.0% | At Least One Post-Baseline Value Below LLN |  |
| classification | VARCHAR | 19.8% | #17/Stable Disease : VEGRfR2 Expression |  |
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| result_group_id | BIGINT | 0.0% | 854934736 | Joins to result_groups.id |
| outcome_id | BIGINT | 0.0% | 263564255 | Joins to outcomes.id |
| nct_id | VARCHAR | 0.0% | NCT00643617 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1965990240 | Table primary key (auto-increment) |

## outcomes

Outcome measure descriptions and time frames

Source file: `outcomes.txt`
Rows: 666,333

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| param_type | VARCHAR | 7.2% | NUMBER |  |
| dispersion_type | VARCHAR | 39.3% | Standard Deviation |  |
| units_analyzed | VARCHAR | 98.0% | Fallopian tubes |  |
| units | VARCHAR | 7.2% | mg/cm^3 |  |
| anticipated_posting_month_year | VARCHAR | 99.1% | 2009-03 |  |
| anticipated_posting_date | DATE | 99.1% | 2009-03-01 |  |
| population | VARCHAR | 24.8% | Subjects 4 and 9 are in the non-surgical radiation group and only have values... |  |
| time_frame | VARCHAR | 0.0% | Non-surgical arm: baseline, 3 months Surgical arm: baseline, 9 weeks |  |
| description | VARCHAR | 7.3% | Trabecular bone mineral density will be measured in mg/cm3 using volumetric Q... |  |
| title | VARCHAR | 0.0% | Percent of Participants With an Average Daily Abdominal Pain Score ≤ 1 Point,... |  |
| outcome_type | VARCHAR | 0.0% | PRIMARY |  |
| nct_id | VARCHAR | 0.0% | NCT02025634 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 263724631 | Table primary key (auto-increment) |

## overall_officials

People responsible for overall scientific leadership

Source file: `overall_officials.txt`
Rows: 534,026

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| affiliation | VARCHAR | 0.5% | Unviersity of Colorado, Aurora |  |
| name | VARCHAR | 0.0% | Katherine L Dickinson, PhD |  |
| role | VARCHAR | 0.3% | PRINCIPAL_INVESTIGATOR |  |
| nct_id | VARCHAR | 0.0% | NCT03617952 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 215117924 | Table primary key (auto-increment) |

## participant_flows

Recruitment and pre-assignment details

Source file: `participant_flows.txt`
Rows: 80,079

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| units_analyzed | VARCHAR | 98.2% | Eyes |  |
| pre_assignment_details | VARCHAR | 60.9% | A total of 436 participants were randomized and treated in this study with a ... |  |
| recruitment_details | VARCHAR | 59.5% | From all recruitment methods, 25 caregivers were interested in the interventi... |  |
| nct_id | VARCHAR | 0.0% | NCT01818141 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 31119896 | Table primary key (auto-increment) |

## pending_results

Events related to submission of results for QC review

Source file: `pending_results.txt`
Rows: 33,534

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| event_date | DATE | 1.2% | 2020-11-03 |  |
| event_date_description | DATE | 1.2% | 2020-11-03 |  |
| event | VARCHAR | 0.0% | RELEASE |  |
| nct_id | VARCHAR | 0.0% | NCT03064165 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 13256559 | Table primary key (auto-increment) |

## provided_documents

Protocol, SAP, and informed consent form documents

Source file: `provided_documents.txt`
Rows: 85,636

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| url | VARCHAR | 0.0% | https://ClinicalTrials.gov/ProvidedDocs/16/NCT03865316/Prot_SAP_000.pdf |  |
| document_date | DATE | 0.0% | 2021-02-02 |  |
| has_sap | BOOLEAN | 0.0% | true |  |
| has_icf | BOOLEAN | 0.0% | false |  |
| has_protocol | BOOLEAN | 0.0% | true |  |
| document_type | VARCHAR | 0.0% | Study Protocol and Statistical Analysis Plan |  |
| nct_id | VARCHAR | 0.0% | NCT03865316 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 29811673 | Table primary key (auto-increment) |

## reported_event_totals

Totals of reported adverse events by category

Source file: `reported_event_totals.txt`
Rows: 604,152

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| updated_at | TIMESTAMP | 0.0% | 2026-09-13 00:08:14.602236 |  |
| created_at | TIMESTAMP | 0.0% | 2026-09-13 00:08:14.602236 |  |
| subjects_at_risk | BIGINT | 12.0% | 4 |  |
| subjects_affected | BIGINT | 11.7% | 0 |  |
| classification | VARCHAR | 0.0% | Total, serious adverse events |  |
| event_type | VARCHAR | 0.0% | other |  |
| ctgov_group_code | VARCHAR | 0.0% | EG004 |  |
| nct_id | VARCHAR | 0.0% | NCT00802503 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 231914752 | Table primary key (auto-increment) |

## reported_events

Summary of reported adverse events

Source file: `reported_events.txt`
Rows: 12,034,973

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| assessment | VARCHAR | 2.1% | SYSTEMATIC_ASSESSMENT |  |
| vocab | VARCHAR | 11.0% | 22.0 |  |
| frequency_threshold | BIGINT | 0.0% | 0 |  |
| adverse_event_term | VARCHAR | 0.0% | Hypermagnesemia |  |
| organ_system | VARCHAR | 0.0% | Metabolism and nutrition disorders |  |
| event_count | BIGINT | 56.1% | 0 |  |
| description | VARCHAR | 32.8% | 66 patients enrolled, 64 reported for adverse events as 1 patient was ineligi... |  |
| subjects_at_risk | BIGINT | 0.0% | 64 |  |
| subjects_affected | BIGINT | 0.8% | 9 |  |
| default_assessment | VARCHAR | 100.0% |  |  |
| default_vocab | VARCHAR | 100.0% |  |  |
| event_type | VARCHAR | 0.0% | other |  |
| time_frame | VARCHAR | 11.9% | Up to 33 days |  |
| ctgov_group_code | VARCHAR | 0.0% | EG000 |  |
| result_group_id | BIGINT | 0.0% | 855688719 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT00077207 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 273504751 | Table primary key (auto-increment) |

## responsible_parties

Parties responsible for submitting study information

Source file: `responsible_parties.txt`
Rows: 584,077

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| old_name_title | VARCHAR | 95.7% | Disclosures Group |  |
| affiliation | VARCHAR | 56.9% | Massachusetts General Hospital |  |
| organization | VARCHAR | 95.7% | Kai Medical, Inc. |  |
| title | VARCHAR | 56.9% | Principal Investigator |  |
| name | VARCHAR | 56.9% | Michael J. Birrer,M.D.,Ph.D. |  |
| responsible_party_type | VARCHAR | 4.3% | SPONSOR |  |
| nct_id | VARCHAR | 0.0% | NCT01672541 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 233523082 | Table primary key (auto-increment) |

## result_agreements

Agreements between sponsor and principal investigators about results

Source file: `result_agreements.txt`
Rows: 80,079

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| restrictive_agreement | BOOLEAN | 23.4% | false |  |
| other_details | VARCHAR | 72.6% | Bristol-Myers Squibb Co. agreements with investigators vary; constant is our ... |  |
| restriction_type | VARCHAR | 62.1% | OTHER |  |
| agreement | VARCHAR | 100.0% |  |  |
| pi_employee | BOOLEAN | 0.0% | true |  |
| nct_id | VARCHAR | 0.0% | NCT03940508 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 31980632 | Table primary key (auto-increment) |

## result_contacts

Points of contact for scientific information about results

Source file: `result_contacts.txt`
Rows: 80,079

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| extension | VARCHAR | 94.7% | 50525 |  |
| email | VARCHAR | 6.0% | shrobb@iu.edu |  |
| phone | VARCHAR | 4.5% | 317-274-3152 |  |
| name | VARCHAR | 0.0% | Dr. Sheri Robb, MT-BC |  |
| organization | VARCHAR | 0.0% | Indiana University School of Nursing |  |
| nct_id | VARCHAR | 0.0% | NCT03085927 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 31981019 | Table primary key (auto-increment) |

## result_groups

Aggregate list of group titles/descriptions for results reporting

Source file: `result_groups.txt`
Rows: 2,217,791

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| outcome_id | BIGINT | 28.7% | 263983039 | Joins to outcomes.id |
| description | VARCHAR | 0.8% | Intervention Period 1: Placebo Intervention period 2: 4mg PP 1420 Interventio... |  |
| title | VARCHAR | 0.0% | MCI-186 - Placebo of MCI-186 |  |
| result_type | VARCHAR | 0.0% | Outcome |  |
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| nct_id | VARCHAR | 0.0% | NCT00424463 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 856309949 | Table primary key (auto-increment) |

## retractions

Retraction notices for study results or publications

Source file: `retractions.txt`
Rows: 335

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| nct_id | VARCHAR | 0.0% | NCT01543815 | Primary trial identifier, joins across all AACT tables |
| source | VARCHAR | 0.0% | Trials. 2018 Dec 20;19(1):692 |  |
| pmid | BIGINT | 0.0% | 30572914 |  |
| reference_id | BIGINT | 0.0% | 438900445 |  |
| id | BIGINT | 0.0% | 141464 | Table primary key (auto-increment) |

## search_term_results

Source file: `search_term_results.txt`
Rows: 513,966

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| updated_at | TIMESTAMP | 0.0% | 2026-09-14 04:25:33.997427 |  |
| created_at | TIMESTAMP | 0.0% | 2026-09-14 04:25:33.997406 |  |
| search_term_id | BIGINT | 0.0% | 45 |  |
| nct_id | VARCHAR | 0.0% | NCT00000758 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 284185213 | Table primary key (auto-increment) |

## search_terms

Source file: `search_terms.txt`
Rows: 186

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| updated_at | TIMESTAMP | 0.0% | 2025-01-28 21:03:58.475729 |  |
| created_at | TIMESTAMP | 0.0% | 2025-01-28 21:03:58.475729 |  |
| group | VARCHAR | 0.0% | diseases of the heart |  |
| term | VARCHAR | 0.0% | rheumatic fever without mention of heart involvement |  |
| id | BIGINT | 0.0% | 1 | Table primary key (auto-increment) |

## sponsors

Sponsor and collaborator names and types

Source file: `sponsors.txt`
Rows: 960,579

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | University of California, Irvine |  |
| lead_or_collaborator | VARCHAR | 0.0% | lead |  |
| agency_class | VARCHAR | 0.1% | OTHER |  |
| nct_id | VARCHAR | 0.0% | NCT03624348 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 385929686 | Table primary key (auto-increment) |

## studies

Core study record: title, status, phase, type, dates, enrollment, and regulatory info

Source file: `studies.txt`
Rows: 602,514

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| patient_registry | BOOLEAN | 80.8% | false |  |
| baseline_type_units_analyzed | VARCHAR | 99.9% | Clusters |  |
| fdaaa801_violation | VARCHAR | 100.0% | t |  |
| expanded_access_status_for_nctid | VARCHAR | 99.9% | AVAILABLE |  |
| expanded_access_nctid | VARCHAR | 99.9% | NCT03123029 |  |
| delayed_posting | BOOLEAN | 99.8% | true |  |
| source_class | VARCHAR | 0.2% | OTHER |  |
| updated_at | TIMESTAMP | 0.0% | 2026-09-12 10:38:28.630718 |  |
| created_at | TIMESTAMP | 0.0% | 2026-09-12 10:38:28.630718 |  |
| plan_to_share_ipd_description | VARCHAR | 85.0% | CSL will consider requests to share Individual Patient Data (IPD) from system... |  |
| plan_to_share_ipd | VARCHAR | 47.2% | NO |  |
| ipd_url | VARCHAR | 97.8% | http://novonordisk-trials.com |  |
| ipd_access_criteria | VARCHAR | 94.9% | Requests may only be made by systematic review groups or bona-fide researcher... |  |
| ipd_time_frame | VARCHAR | 94.5% | IPD requests may be submitted to CSL no earlier than 12 months after publicat... |  |
| biospec_description | VARCHAR | 95.4% | From peripheral blood samples, the DNA extraction following the protocol sali... |  |
| biospec_retention | VARCHAR | 95.4% | SAMPLES_WITH_DNA |  |
| is_us_export | BOOLEAN | 87.6% | false |  |
| is_ppsd | VARCHAR | 100.0% | t |  |
| is_unapproved_device | BOOLEAN | 99.1% | true |  |
| is_fda_regulated_device | BOOLEAN | 37.2% | false |  |
| is_fda_regulated_drug | BOOLEAN | 37.1% | false |  |
| has_dmc | BOOLEAN | 17.7% | true |  |
| expanded_access_type_treatment | BOOLEAN | 100.0% | true |  |
| expanded_access_type_intermediate | BOOLEAN | 100.0% | true |  |
| expanded_access_type_individual | BOOLEAN | 99.9% | true |  |
| has_expanded_access | BOOLEAN | 1.2% | false |  |
| why_stopped | VARCHAR | 92.2% | We were unable to obtain the intended sample size. |  |
| number_of_groups | BIGINT | 84.6% | 1 |  |
| number_of_arms | BIGINT | 27.7% | 1 |  |
| limitations_and_caveats | VARCHAR | 97.2% | One subject completed the protocol, and the FDA placed the study on hold due ... |  |
| source | VARCHAR | 0.0% | Kırıkkale University |  |
| enrollment_type | VARCHAR | 2.8% | ESTIMATED |  |
| enrollment | BIGINT | 1.2% | 30 |  |
| phase | VARCHAR | 23.7% | NA |  |
| last_known_status | VARCHAR | 83.9% | RECRUITING |  |
| overall_status | VARCHAR | 0.0% | UNKNOWN |  |
| official_title | VARCHAR | 1.7% | Determination of Physical Activity Levels,Quality of Life,Depression and Fati... |  |
| brief_title | VARCHAR | 0.0% | Determination Physical Activity Levels,Quality Life,Depression and Fatigue Se... |  |
| baseline_population | VARCHAR | 95.5% | The Full Analysis Set (FAS) included all subjects who were randomized to a st... |  |
| acronym | VARCHAR | 70.9% | ICT-HCT |  |
| study_type | VARCHAR | 0.2% | INTERVENTIONAL |  |
| target_duration | VARCHAR | 97.1% | 4 Days |  |
| primary_completion_date | DATE | 3.6% | 2021-02-28 |  |
| primary_completion_date_type | VARCHAR | 3.6% | ESTIMATED |  |
| primary_completion_month_year | VARCHAR | 3.6% | 2021-02 |  |
| completion_date | DATE | 2.8% | 2022-01-01 |  |
| completion_date_type | VARCHAR | 3.9% | ESTIMATED |  |
| completion_month_year | VARCHAR | 2.8% | 2022-01-01 |  |
| verification_date | DATE | 0.2% | 2018-08-31 |  |
| verification_month_year | VARCHAR | 0.2% | 2018-08 |  |
| start_date | DATE | 0.9% | 2018-12-01 |  |
| start_date_type | VARCHAR | 30.9% | ESTIMATED |  |
| start_month_year | VARCHAR | 0.9% | 2021-12-15 |  |
| last_update_posted_date_type | VARCHAR | 0.0% | ACTUAL |  |
| last_update_posted_date | DATE | 0.0% | 2023-11-07 |  |
| last_update_submitted_qc_date | DATE | 0.0% | 2018-08-07 |  |
| disposition_first_posted_date_type | VARCHAR | 98.4% | ESTIMATED |  |
| disposition_first_posted_date | DATE | 98.4% | 2017-02-02 |  |
| disposition_first_submitted_qc_date | DATE | 98.7% | 2015-11-03 |  |
| results_first_posted_date_type | VARCHAR | 86.7% | ACTUAL |  |
| results_first_posted_date | DATE | 86.7% | 2021-04-19 |  |
| results_first_submitted_qc_date | DATE | 86.7% | 2021-03-23 |  |
| study_first_posted_date_type | VARCHAR | 0.0% | ESTIMATED |  |
| study_first_posted_date | DATE | 0.0% | 2015-01-26 |  |
| study_first_submitted_qc_date | DATE | 0.0% | 2015-01-22 |  |
| last_update_submitted_date | DATE | 0.0% | 2024-11-25 |  |
| disposition_first_submitted_date | DATE | 98.4% | 2016-04-26 |  |
| results_first_submitted_date | DATE | 86.7% | 2010-11-09 |  |
| study_first_submitted_date | DATE | 0.0% | 2015-01-16 |  |
| nlm_download_date_description | VARCHAR | 100.0% |  |  |
| nct_id | VARCHAR | 0.0% | NCT05184634 | Primary trial identifier, joins across all AACT tables |

## study_references

Citations to publications related to the study

Source file: `study_references.txt`
Rows: 1,140,181

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| citation | VARCHAR | 0.0% | Arendt-Nielsen L, Madsen H, Jarrell J, Gregersen H, Drewes AM. Pain evoked by... |  |
| reference_type | VARCHAR | 0.0% | RESULT |  |
| pmid | BIGINT | 5.1% | 24773180 |  |
| nct_id | VARCHAR | 0.0% | NCT03279224 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 439539974 | Table primary key (auto-increment) |
